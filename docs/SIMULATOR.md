# Native Rockbox simulator on this Mac

The official `ipodvideo` UI simulator runs Rockbox against a local `simdisk` folder. It uses the native skin renderer, menu logic, codecs, and plugins, with simulated input and hardware. It is suitable for layout, parser, playback-state, and navigation checks. It is not a full hardware emulator and cannot establish physical storage reliability, charging behavior, battery runtime, screen pressure, or iPod CPU performance.

## Local setup

- Source: official [Rockbox mirror](https://github.com/Rockbox/rockbox), commit `e45936397ee3677c910c9a0c6473184e9755040c`, with the local host/experimental patches described below.
- Host: Apple Silicon macOS. GCC 16.2.0 was installed with Homebrew; SDL2 compatibility runtime 2.32.72 was already available.
- Target: `ipodvideo`, 320 × 240, simulator build; not `ipod6g`.
- Source, builds, logs, and virtual storage: ignored `local/rockbox/`.
- On modern macOS, upstream configure uses SDL threads because `sigaltstack` is restricted. No macOS security setting was disabled.

From the project root, the initial build was:

```sh
git clone --depth 1 https://github.com/Rockbox/rockbox.git local/rockbox/source
mkdir -p local/rockbox/build-ipodvideo
cd local/rockbox/build-ipodvideo
../source/tools/configure --target=ipodvideo --type=s --no-ccache
make -j8
make install
```

The clone command is for a fresh checkout only. To reproduce this exact source after cloning, check out the recorded commit. Host dependency installation is separate from project scripts.

## Iterate

```sh
python3 tools/simulator.py stage piplupos
python3 tools/simulator.py run
```

Select the staged skin in **Settings → Theme Settings → Browse Themes**. After editing, stage again and reselect the theme to reload it. Simulator keyboard mappings are in `local/rockbox/source/uisimulator/buttonmap/ipod.c`; use computer-use tools to interact with the app. Keep test music in `local/rockbox/build-ipodvideo/simdisk/Music`.

Only themes are staged by this helper. It never detects, formats, mounts, or writes to a physical device. Do not copy simulator firmware or plugins to the real iPod; they are compiled for the Mac.

## Installed Apple Silicon apps

Both executables were checked as native ARM64 and opened through computer use:

- `/Applications/RockboxUtility.app`: locally compiled current-source Utility 1.5.2 using Qt 6.11.2. The official released 1.5.1 Mac download was Intel-only; this is not an official released ARM binary. Its bundled signature verification passed. The app is currently unconfigured; no install has been started against the HFS+ iPod.
- `/Applications/PiplupOS Simulator.app`: the native ipodvideo simulator, with a virtual disk at `Contents/Resources/simdisk`. This installed app uses a snapshot separate from the project's `local/rockbox/build-ipodvideo/simdisk`.

The CLI loop above uses the project disk via `--root`. To refresh the installed app during development, close only the simulator, copy the desired generated theme files/assets into its virtual `.rockbox`, then reopen it and reselect the theme. Updating project themes does not automatically update that installed snapshot. Never copy the simulator's `.rockbox` to the iPod.

Keyboard controls: Up/Down scroll, Return selects, Left goes back, Escape opens the menu, Space plays/pauses, and F5 saves a native-resolution screen dump to the virtual disk. The physical click-wheel drawing is a simulator input guide, not the actual theme.

The native Utility build used Homebrew's `qtbase`, `qt5compat`, `qtsvg` and `qttools`. Build commands from the repository root:

```sh
cmake -S local/rockbox/source/utils -B local/rockbox/build-utility-arm64 \
  -DCMAKE_BUILD_TYPE=Release -DCMAKE_OSX_ARCHITECTURES=arm64 \
  -DQt6Core5Compat_DIR=/opt/homebrew/opt/qt5compat/lib/cmake/Qt6Core5Compat \
  -DQt6Svg_DIR=/opt/homebrew/opt/qtsvg/lib/cmake/Qt6Svg \
  -DQt6SvgWidgets_DIR=/opt/homebrew/opt/qtsvg/lib/cmake/Qt6SvgWidgets \
  -DQt6LinguistTools_DIR=/opt/homebrew/opt/qttools/lib/cmake/Qt6LinguistTools
cmake --build local/rockbox/build-utility-arm64 --target RockboxUtility -j8
/opt/homebrew/opt/qtbase/bin/macdeployqt \
  local/rockbox/build-utility-arm64/rbutilqt/RockboxUtility.app -codesign=-
```

Installation into Applications was a separate authorized Mac setup step; project scripts remain local-only. Build logs and the original Intel release app are retained under ignored `local/rockbox/`.

## Recorded local source patch

`tools/patches/macos-simulator.patch` records the changes relative to the pinned source:

- Installed-app defaults locate the simulated disk and official `UI256.bmp` inside the app bundle.
- Mac simulator key releases preserve a minimum 30 ms input pulse so fast computer-use taps reach Rockbox's polling loop. The guard excludes hardware builds.
- The desktop database tool includes the SDL filesystem implementation needed to link this macOS build.
- The simulator target enables HAVE_SKIN_VARIABLES for the experimental delayed-headphone skin. Stock ipodvideo does not enable it; upstream enables the feature for touchscreen targets. No custom device firmware has been compiled or installed.
- Mac-only preview refresh: playback waits and idle list waits are capped at 50 ms, menu skin updates use a 50 ms default delay, and an alternator deadline equal to the current tick counts as expired. These changes are guarded by SIMULATOR and __APPLE__; physical builds keep upstream scheduling. The theme requests 100 ms frames, a nominal 10-frame/s target, not a measured hardware rate.

Apply this patch from a clean checkout of the recorded commit before reproducing these modified builds. The installed-app paths are specific to this Mac. This is a patched simulator using the native Rockbox renderer, not a stock-release hardware test.

## Verified native prototype

Both WPS/SBS pairs passed `checkwps.ipodvideo`. Through the actual GUI, the full standard menu, nested settings/file browsing, AAC playback from an Apple-style sync path, WAV playback, scrolling filename fallback, missing artist/album fallback, pause, pool frames and mascot states were checked. The experimental WPS showed a delayed neck-rest state and headphones back on after resume. Native 320 × 240 F5 dumps are saved in `design/piplupos/previews/`.

`piplupos` uses standard timed sublines and immediate neck rest on pause. `piplupos-delayed` requires the custom feature and retains a draft 3-second delay. Normal delay/resume verification does not establish rapid cancellation, stopped-state behavior, cross-screen persistence, stable 4.0 compatibility or hardware performance. The menu mascot uses immediate playback conditionals in both versions.

The current water animation has 12 phases with a continuous angular loop, replacing the four-phase wrap jump. The title bar, artist and album use a bundled Helvetica Bold font; package/staging helpers now include validated RB12 font files and their license. Bold text, standard pause/resume, no-cover playback, menu navigation and the experimental normal pause delay/resume were rechecked after the faster Mac build. The animation preview GIF holds native text still and composites exported frames; it is not a simulator recording or a frame-rate measurement.

## Checks before calling a theme ready

- Load both WPS and SBS through the actual skin parser; check logs for fallback/errors.
- Verify play, pause, stop, seeking, resume, and quick repeated state changes.
- Check headphone delay cancellation and one-shot transitions, including leaving and reentering playback.
- Verify long/missing metadata, elapsed/remaining time, battery, volume, repeat, and shuffle.
- Navigate the complete menu and file browser; preserve entry points to every standard feature.
- Review at 1× native resolution as well as enlarged screenshots.
- Confirm the eventual hardware Rockbox version supports every tag used; this simulator is a development revision, while the current stable device release is 4.0.
- Later test both firmware boot paths, codecs, SD writes, charging, animation cost, and playback responsiveness on the actual iPod.

## Installation boundary

On 2026-10-01 the connected 128 GB iPod was still HFS+ and had approximately 11.9 GB in use. Rockbox installation needs a FAT32-initialized iPod. No formatting, bootloader install, reset, or disconnection was performed. Preserve the Mac song originals and review backups before a conversion that may erase the iPod.

Rodrigo approved dual boot and Mac preparation, and requested no resets/unplugging during autonomous work. Ask before pushing to main. A hardware installation session is separate from the local simulator loop.

Primary references: [official simulator instructions](https://github.com/Rockbox/rockbox/blob/master/docs/UISIMULATOR), [Mac build configuration](https://github.com/Rockbox/rockbox/blob/master/tools/configure), [installation requirements](https://github.com/Rockbox/rockbox/blob/master/manual/getting_started/installation.tex).
