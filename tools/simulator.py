#!/usr/bin/env python3
"""Stage theme packages and run the local ipodvideo simulator. No device access."""
import argparse
import subprocess
import zipfile
from pathlib import Path

import modpod

BUILD = modpod.ROOT / "local" / "rockbox" / "build-ipodvideo"


def stage(slug):
    theme = modpod.load_theme(slug)
    simdisk = modpod.inside_repo(BUILD / "simdisk")
    if not (simdisk / ".rockbox" / "rockbox-info.txt").is_file():
        raise ValueError("Build and install the simulator first; see docs/SIMULATOR.md.")
    package = modpod.package_theme(theme)
    allowed = {f".rockbox/themes/{slug}.cfg", f".rockbox/wps/{slug}.wps", f".rockbox/wps/{slug}.sbs"}
    allowed.update(f".rockbox/fonts/{relative.name}" for relative, _ in modpod.theme_resources(slug)
                   if relative.parts[0] == "fonts")
    assets = f".rockbox/wps/{slug}/"
    with zipfile.ZipFile(package) as archive:
        targets = []
        for member in archive.infolist():
            if member.filename not in allowed and not member.filename.startswith(assets):
                raise ValueError(f"Unexpected theme member: {member.filename}")
            target = modpod.inside_repo(simdisk / member.filename)
            if not target.is_relative_to(simdisk):
                raise ValueError("Theme member leaves simulator storage.")
            targets.append((member, target))
        for member, target in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(member))
    print(f"Staged {theme['name']} in {simdisk}; choose it under Settings > Theme Settings > Browse Themes.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    load = commands.add_parser("stage")
    load.add_argument("slug")
    commands.add_parser("run")
    args = parser.parse_args()
    try:
        if args.command == "stage":
            stage(args.slug)
        else:
            binary = modpod.inside_repo(BUILD / "rockboxui")
            if not binary.is_file():
                raise ValueError("Build the simulator first; see docs/SIMULATOR.md.")
            subprocess.run([str(binary), "--root", str(BUILD / "simdisk"), "--zoom", "3", "--debugwps"], cwd=BUILD, check=True)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
