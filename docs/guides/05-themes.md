<!-- Generated from handbook/content.json by tools/modpod.py build. -->
# Make it your own

PiplupOS is the custom design direction. Paper and Midnight are scaffold examples for learning the native theme workflow.

## Before starting

PiplupOS now runs in the native Mac simulator: light-grey windows, blue pool animation, the round-face mascot, full menu access and playback metadata. The standard skin changes immediately on pause; the experimental 3-second headphone delay requires custom firmware and was checked in the modified simulator. Editable Aseprite sources live in design/piplupos/. Dual boot with Apple firmware is approved; no Rockbox or theme has been installed on the iPod.

## 1. Create a theme folder

Run python3 tools/modpod.py new my-theme --from piplupos. This copies its editable manifest, native layout overrides and bitmap assets into themes/my-theme/ without overwriting an existing theme. Use paper for a simpler built-in-font example.

## 2. Edit the palette or layout

Change text colors and the name in theme.json, or download a manifest from the palette editor. Edit themes/my-theme/native/ for its own layout. PiplupOS chrome and sprites are bitmaps: recolor them in Aseprite and export separately; manifest edits do not recolor the art. Its Helvetica font is included in the prepared stable firmware ZIP.

## 3. Build the package

Run python3 tools/modpod.py build my-theme. The ZIP in dist/themes/ contains configuration, playback and menu/status skins, plus the theme's BMP assets. The command refreshes this handbook and checks package structure; native renderer checks are separate.

## 4. Try it in Rockbox

Use python3 tools/simulator.py stage my-theme and the local simulator workflow in docs/SIMULATOR.md. Select the theme under Settings → Theme Settings → Browse Theme Files. Shuffle the indexed library through Database → Shuffle Songs. Shuffle and Repeat for the current playlist are under Settings → Playback Settings. Test long titles, missing tags, play/pause, battery, volume and menu scrolling. Later merge the package into an existing working iPod Rockbox installation, preserving its firmware. Do not use the experimental timers variant with stock firmware.

## Checklist

- [x] First custom manifest created
- [x] Theme package built and inspected
- [x] Native skin tested in a simulator or on the iPod
- [ ] Device playback and menus tested; findings logged

## Keep in mind

PiplupOS native checks are recorded in docs/BUILD_LOG.md; Paper and Midnight have structural checks only. The browser preview is a generic illustration. Stable 4.0 compatibility, final pixel cleanup, Suki's cameo, early boot branding and physical playback/animation costs remain pending.

## Full references

- [Rockbox manual · Theme and skin configuration](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch13.html)
- [Rockbox manual · Skin tag reference](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildap4.html)
- [Aseprite · Official batch processing and export documentation](https://github.com/aseprite/docs/blob/main/cli.md)
