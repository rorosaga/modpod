#!/usr/bin/env python3
"""Local-only Modpod theme and handbook tools. Python standard library only."""

import argparse
import base64
import functools
import json
import mimetypes
import re
import shutil
import sys
import tempfile
import zipfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from string import Template
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
COLOR = re.compile(r"[0-9a-fA-F]{6}\Z")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_slug(value):
    if not isinstance(value, str) or len(value) > 48 or not SLUG.fullmatch(value):
        raise ValueError("Use a theme slug of at most 48 lowercase letters/digits, separated by hyphens.")
    return value


def inside_repo(path):
    resolved = path.resolve()
    if not resolved.is_relative_to(ROOT.resolve()):
        raise ValueError(f"Path leaves the repository: {path}")
    return resolved


def write_text(path, value):
    inside_repo(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def load_theme(slug):
    check_slug(slug)
    folder = ROOT / "themes" / slug
    if folder.is_symlink():
        raise ValueError(f"Theme folders must not be symbolic links: {slug}")
    path = inside_repo(folder / "theme.json")
    theme = read_json(path)
    if theme.get("slug") != slug:
        raise ValueError(f"Theme folder and manifest slug differ: {slug}")
    if theme.get("target") != "ipodvideo" or theme.get("screen") != [320, 240]:
        raise ValueError(f"{slug}: target must be ipodvideo, screen must be [320, 240].")
    for key in ("name", "description", "status"):
        value = theme.get(key)
        if not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"{slug}: {key} must be a nonempty single line.")
    colors = theme.get("colors", {})
    if not isinstance(colors, dict) or set(colors) != {"background", "foreground", "accent", "muted"}:
        raise ValueError(f"{slug}: supply background, foreground, accent, and muted colors.")
    for key, value in colors.items():
        if not isinstance(value, str) or not COLOR.fullmatch(value):
            raise ValueError(f"{slug}: {key} must be six hexadecimal digits without #.")
        colors[key] = value.upper()
    return theme


def all_themes():
    return [load_theme(path.name) for path in sorted((ROOT / "themes").iterdir()) if path.is_dir()]


def https_url(value):
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username


def photo_data(value):
    if https_url(value):
        return value
    path = inside_repo(ROOT / value)
    if not path.is_relative_to((ROOT / "hardware" / "photos").resolve()):
        raise ValueError("Local product photos must be under hardware/photos/.")
    mime = mimetypes.guess_type(path.name)[0]
    if mime not in ("image/png", "image/jpeg", "image/webp"):
        raise ValueError(f"Use PNG, JPEG, or WebP product photos: {value}")
    if path.stat().st_size > 5_000_000:
        raise ValueError(f"Reduce product photo below 5 MB: {value}")
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def project_data():
    content = read_json(ROOT / "handbook" / "content.json")
    sources = read_json(ROOT / "references" / "sources.json")
    parts = read_json(ROOT / "hardware" / "parts.json")
    device = read_json(ROOT / "hardware" / "device.json")
    ids = [source["id"] for source in sources]
    if len(set(ids)) != len(ids):
        raise ValueError("Source IDs must be unique.")
    for source in sources:
        if not https_url(source["url"]):
            raise ValueError(f"Source URL must use HTTPS: {source['id']}")
    seen = set()
    for stage in content["stages"]:
        check_slug(stage["id"])
        if stage["id"] in seen:
            raise ValueError("Stage IDs must be unique.")
        seen.add(stage["id"])
        if set(stage["sources"]) - set(ids):
            raise ValueError(f"Unknown source in stage: {stage['id']}")
        task_ids = [task["id"] for task in stage["checklist"]]
        if len(set(task_ids)) != len(task_ids):
            raise ValueError(f"Duplicate checklist ID: {stage['id']}")
        for task_id in task_ids:
            check_slug(task_id)
    part_ids = [part["id"] for part in parts]
    if len(set(part_ids)) != len(part_ids):
        raise ValueError("Part IDs must be unique.")
    for part in parts:
        if part["source"] not in ids or not https_url(part["url"]):
            raise ValueError(f"Invalid part link: {part['id']}")
        part["image"] = photo_data(part["image"])
    return {"content": content, "sources": sources, "parts": parts, "device": device, "themes": all_themes()}


def new_theme(slug, source):
    check_slug(slug)
    theme = load_theme(source)
    target = ROOT / "themes" / slug
    inside_repo(target)
    if target.exists() or target.is_symlink():
        raise ValueError(f"Theme already exists; nothing overwritten: {slug}")
    resources = theme_resources(source)
    theme.update(slug=slug, name=slug.replace("-", " ").title(), status="Draft · not tested in Rockbox")
    target.mkdir()
    write_text(target / "theme.json", json.dumps(theme, indent=2, ensure_ascii=False) + "\n")
    for relative, path in resources:
        destination = inside_repo(target / relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, destination)
    print(f"Created themes/{slug}/theme.json from {source}.")


def theme_resources(slug):
    """Check every resource before copying or packaging; never follow symlinks."""
    folder = ROOT / "themes" / check_slug(slug)
    resources = []
    for name in ("native", "assets", "fonts"):
        root = folder / name
        if root.is_symlink():
            raise ValueError(f"Theme resource folders must not be symlinks: {root}")
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Theme resources must not be symlinks: {path}")
            inside_repo(path)
            if path.is_file():
                relative = path.relative_to(folder)
                if name == "native" and relative.as_posix() not in {
                    "native/theme.cfg.in", "native/theme.wps.in", "native/theme.sbs.in"
                }:
                    raise ValueError(f"Unexpected native template: {relative}")
                if name == "assets" and (path.suffix != ".bmp" or not path.read_bytes().startswith(b"BM")):
                    raise ValueError(f"Native theme assets must be BMP files: {relative}")
                if name == "fonts":
                    if len(relative.parts) != 2 or not (
                        (path.suffix == ".fnt" and path.read_bytes().startswith(b"RB12"))
                        or path.name == "Adobe-Helvetica-LICENSE.txt"
                    ):
                        raise ValueError(f"Theme fonts must be Rockbox RB12 files or their license: {relative}")
                resources.append((relative, path))
    return resources


def package_theme(theme):
    slug = theme["slug"]
    tokens = dict(theme["colors"], slug=slug, name=theme["name"])
    members = {}
    resources = dict(theme_resources(slug))
    for template, destination in (
        ("theme.cfg.in", f".rockbox/themes/{slug}.cfg"),
        ("theme.wps.in", f".rockbox/wps/{slug}.wps"),
        ("theme.sbs.in", f".rockbox/wps/{slug}.sbs"),
    ):
        source = resources.get(Path("native") / template, ROOT / "templates" / "ipodvideo" / template)
        text = inside_repo(source).read_text(encoding="utf-8")
        members[destination] = Template(text).substitute(tokens).encode("utf-8")
    for relative, path in resources.items():
        if relative.parts[0] == "assets":
            members[f".rockbox/wps/{slug}/{relative.relative_to('assets').as_posix()}"] = path.read_bytes()
        elif relative.parts[0] == "fonts":
            members[f".rockbox/fonts/{relative.name}"] = path.read_bytes()
    output = ROOT / "dist" / "themes" / f"{slug}.zip"
    inside_repo(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output.parent, suffix=".zip", delete=False) as handle:
        temp_path = Path(handle.name)
    try:
        with zipfile.ZipFile(temp_path, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, value in sorted(members.items()):
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, value)
        with zipfile.ZipFile(temp_path) as archive:
            if set(archive.namelist()) != set(members) or archive.testzip() is not None:
                raise ValueError(f"Theme archive verification failed: {slug}")
        temp_path.replace(output)
    finally:
        temp_path.unlink(missing_ok=True)
    print(f"Built dist/themes/{slug}.zip (structure checked; native results are recorded separately in docs/BUILD_LOG.md).")
    return output


def build_guides(data):
    sources = {source["id"]: source for source in data["sources"]}
    start = "# Start here\n\nThis is the build order for the iPod Video 5.5. Rodrigo reports the Quad and battery installed and the new capacity working; screen pressure and post-mod checks remain pending. Rockbox is not installed.\n\n"
    for stage in data["content"]["stages"]:
        filename = f"{stage['number']}-{stage['id']}.md"
        start += f"{int(stage['number'])}. [{stage['title']}](guides/{filename}) — {stage['summary']}\n"
        guide = f"<!-- Generated from handbook/content.json by tools/modpod.py build. -->\n# {stage['title']}\n\n{stage['summary']}\n\n## Before starting\n\n{stage['before']}\n\n"
        for i, step in enumerate(stage["steps"], 1):
            guide += f"## {i}. {step['title']}\n\n{step['body']}\n\n"
        guide += "## Checklist\n\n"
        for task in stage["checklist"]:
            guide += f"- [{'x' if task.get('complete') else ' '}] {task['text']}\n"
        guide += f"\n## Keep in mind\n\n{stage['note']}\n\n## Full references\n\n"
        for source_id in stage["sources"]:
            source = sources[source_id]
            guide += f"- [{source['title']}]({source['url']})\n"
        write_text(ROOT / "docs" / "guides" / filename, guide)
    start += "\nUse [the build log](BUILD_LOG.md) for durable test results, [recovery notes](RECOVERY.md) for problems, and [the theme workflow](THEME_WORKFLOW.md) for design work.\n\nGuides are generated from `handbook/content.json`; edit that source and rebuild.\n"
    write_text(ROOT / "docs" / "START_HERE.md", start)
    watchlist = "# Tutorial watchlist\n\nVideo titles/descriptions checked on 2026-09-30. Videos have not been watched. No timestamps or exact-hardware fit claims are inferred. Add Rodrigo’s chosen videos here via `references/sources.json`.\n\n"
    for source in data["sources"]:
        if source["kind"].startswith("Video"):
            watchlist += f"## [{source['title']}]({source['url']})\n\n{source['author']} · {source['published']}\n\n{source['note']}\n\n- Watched: pending\n- Useful timestamps: pending\n- Differences from this build: pending review\n\n"
    write_text(ROOT / "references" / "WATCHLIST.md", watchlist.rstrip() + "\n")


def build_handbook(data):
    page = (ROOT / "handbook" / "shell.html").read_text(encoding="utf-8")
    data["native_renders"] = []
    for name, label in (("menu", "PiplupOS complete menu"), ("playing", "PiplupOS AAC playback")):
        path = inside_repo(ROOT / "design" / "piplupos" / "previews" / f"native-{name}-2026-10-01.png")
        if path.is_file():
            data["native_renders"].append({"label": label, "image": "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")})
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    page = page.replace("__DATA__", payload)
    page = page.replace("__STYLE__", (ROOT / "handbook" / "style.css").read_text(encoding="utf-8"))
    page = page.replace("__SCRIPT__", (ROOT / "handbook" / "app.js").read_text(encoding="utf-8"))
    write_text(ROOT / "handbook" / "index.html", page)


def build(slug=None):
    data = project_data()
    selected = [load_theme(slug)] if slug else data["themes"]
    for theme in selected:
        package_theme(theme)
    build_guides(data)
    build_handbook(data)
    print("Refreshed docs/guides, references/WATCHLIST.md, and handbook/index.html.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("new", help="Create an editable theme without overwriting files")
    create.add_argument("slug")
    create.add_argument("--from", dest="source", default="paper")
    commands.add_parser("list", help="List theme manifests")
    commands.add_parser("validate", help="Check project data (not the Rockbox skin parser)")
    package = commands.add_parser("build", help="Build theme ZIPs, guides, and handbook")
    package.add_argument("slug", nargs="?")
    serve = commands.add_parser("serve", help="Build and serve the handbook on loopback only")
    serve.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    try:
        if args.command == "new":
            new_theme(args.slug, args.source)
        elif args.command == "list":
            for theme in all_themes():
                print(f"{theme['slug']:16} {theme['name']} — {theme['status']}")
        elif args.command == "validate":
            data = project_data()
            print(f"Valid: {len(data['themes'])} theme manifests, {len(data['content']['stages'])} guides, {len(data['parts'])} parts, {len(data['sources'])} references.")
            print("Native Rockbox syntax / device behavior not checked.")
        elif args.command == "build":
            build(args.slug)
        elif args.command == "serve":
            build()
            handler = functools.partial(SimpleHTTPRequestHandler, directory=str(ROOT / "handbook"))
            with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
                print(f"Open http://127.0.0.1:{args.port} · Ctrl-C to stop", flush=True)
                server.serve_forever()
    except KeyboardInterrupt:
        print("\nHandbook server stopped.")
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
