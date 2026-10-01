# Theme workshop

The target is `ipodvideo`, 320 × 240 pixels. Themes have a manifest and either shared or theme-specific native templates.

```sh
python3 tools/modpod.py new my-theme --from piplupos
python3 tools/modpod.py build my-theme
```

Each manifest has a slug, display name, description, fixed target/screen, four six-digit RGB colors, and a validation status. Use lowercase letters, digits, and hyphens for slugs. Color values have no leading `#`.

The browser palette editor downloads a manifest; it does not silently edit your repository. Replace the matching `themes/<slug>/theme.json`, then rebuild. Create a separate theme with the CLI first if you want to preserve an original palette.

Shared layouts live in `templates/ipodvideo/`. Theme-specific overrides live in `themes/<slug>/native/`, using the same `theme.cfg.in`, `theme.wps.in` and `theme.sbs.in` names. Editing shared templates changes themes without overrides. The `new` command copies a source theme's manifest, native overrides and bitmaps, refusing to overwrite an existing theme or follow resource symlinks.

PiplupOS backdrops and sprite strips are bitmap artwork: changing manifest text colors does not recolor those images. Edit the Aseprite sources or `design/piplupos/export-native.lua` and export again for chrome/mascot changes. The export script regenerates its native UI sources and bitmaps; keep hand-edited UI variants separately. It does not overwrite the mascot source.

## The ZIP layout

```text
.rockbox/
  themes/my-theme.cfg
  wps/my-theme.wps
  wps/my-theme.sbs
  wps/my-theme/*.bmp
```

Packages include the skin's BMP artwork, but no bootloader, firmware, fonts or music. Installation is a merge into an existing working Rockbox installation, not replacement of the whole `.rockbox` directory. Keep a copy of the previous theme settings so reverting is easy.

## Validation ladder

1. `validate`: JSON schema values, correct target, safe names, reference IDs, and HTTPS/local-photo paths.
2. `build`: generates and checks package structure and file paths. This is **not** a Rockbox syntax check.
3. Simulator and native parser: PiplupOS menu/playback prototypes were checked on 2026-10-01; see `docs/BUILD_LOG.md`. Paper and Midnight still have structural checks only. Recheck modified variants independently.
4. iPod test: confirm layout, long/missing tags, playback states, progress, volume, battery, menus, and USB. Add photos and results to `docs/BUILD_LOG.md`.

The browser preview uses browser font metrics and illustrates the generic palette; it is not the native PiplupOS layout or emulator output. Paper/Midnight use built-in font 0. PiplupOS uses `15-Adobe-Helvetica.fnt`; the prepared stable 4.0 firmware ZIP contains it, and native parser checks flag the font dependency.

Use `piplupos` for the standard-compatible prototype. `piplupos-delayed` requires a custom ipodvideo build enabling HAVE_SKIN_VARIABLES. It is not a drop-in theme for stock firmware. Normal pause delay and resume work in the modified simulator; rapid/cross-screen transitions and the actual device remain unverified. Its menu mascot uses immediate state changes; the delay applies to the playback screen.

To stage a local native test:

```sh
python3 tools/simulator.py stage my-theme
python3 tools/simulator.py run
```

These commands only use the ignored project simulator disk. See `docs/SIMULATOR.md` for the separately installed Mac app and its storage snapshot. Neither helper writes to an iPod.

Primary references: [theme configuration](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch13.html) and [skin tags](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildap4.html).
