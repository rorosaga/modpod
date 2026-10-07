# PiplupOS · Native theme prototype

Rodrigo’s actual theme direction. Paper and Midnight remain scaffolding examples. The mascot is still a pixel-cleanup draft; the native menu/playback layouts now run in the Mac simulator.

## Direction

The main reference is the duck-in-a-pool image inside a Windows 95-style window: **light cool-grey** beveled chrome, deep-blue title bar, and watery cyan/blue content. Rodrigo clarified that the lighter-grey request applies to the UI, not the mascot. The Windows 95 and XP references inform pixel typography, list highlights, small icons, and familiar status bars. Adapt that vocabulary to the iPod’s 320 × 240 screen and click wheel; desktop imagery does not imply mouse, touch, or movable-window functionality.

The generated home screen shows a shortened illustrative menu. The real interface must retain access to all standard functions; do not remove or hide features to reproduce those four rows.

Piplup uses the liked draft’s muted ice-blue, denim-blue, navy, and white palette. Keep him **smaller and chunkier** than the official illustrations. Every state faces **left**, with **closed eyes**. Headphones stay on his head while playing; after a pause/stop delay, he lowers them to his **neck**, and raises them back to his head on resume before bobbing. Three seconds is the draft delay chosen for review, not a final user-specified value. His silhouette should stay readable at 48–64 native pixels tall, leaving room for music and menus.

The first set included four interface/aesthetic references and one visible Piplup sprite. Rodrigo then supplied four more Piplup images to clarify physique: beak, blue collar, two white belly spots, flippers, tail, and feet. These guide anatomy; the smaller chunky draft and its palette remain the selected direction.

**V5 is the current mascot draft.** Rodrigo marked the unwanted white FRONT/LEFT cheek or snout beneath the beak and supplied a preferred example. Follow that example: a compact two-part blue beak with a dark dividing seam, with the white face continuing smoothly around the head underneath it. No protruding white muzzle and no button nose. The darker two-lobed collar sits directly under the chin, separate from the flippers and white belly spots; headphones at neck rest partly overlap it. Playback and headset-transition poses use this face, then were rebuilt in Aseprite with matching neutral height and foot baseline. Faint alpha fringe and disconnected single-pixel specks were removed without recoloring the opaque palette. Earlier attempts remain for comparison.

`aseprite/piplup-timing-v6.aseprite` is the current timing revision of those unchanged v5 pixels: 100 ms playing poses, 200 ms headset-transition poses and the retained 3-second delay. `make-timing-v6.lua` creates that separate source and refuses to overwrite it. V5 remains available for comparison. The current behavior GIF is `previews/piplup-headphones-behavior-v6.gif`.

## Files

- `concepts/mascot-headbob-v1.png`: generated four-pose visual strip, with transparency. A concept reference, not a native sprite sheet.
- `concepts/screens-v1.png`: generated home/now-playing board. Its typography, pixel grid, and layout still need native-size reconstruction.
- `concepts/screens-v2-light-grey.png`: revised light-grey UI, retaining the blue title bars, water, and mascot palette.
- `concepts/screens-v3-round-collar.png`: earlier collar-correction UI board.
- `concepts/screens-v5-preferred-face.png`: current light-grey UI board using the preferred face and two-lobed collar.
- `concepts/mascot-headphones-neck-v2.png`: four generated headset poses: on head, lifted, lowering, resting at neck.
- `concepts/mascot-headbob-v3-round-collar.png` and `concepts/mascot-headphones-neck-v3-round-collar.png`: earlier collar-correction strips. V4 small-beak intermediates also remain.
- `concepts/mascot-headphones-neck-v5-preferred-face.png`: transparent cutout edit of Rodrigo's preferred four-pose reference.
- `concepts/mascot-headbob-v5-preferred-face.png`: playback poses based on that preferred character.
- `aseprite/piplup-draft-v1.aseprite`: earlier 64 × 64 playback-only draft, retained for comparison.
- `aseprite/piplup-draft-v2.aseprite`: earlier 19-frame behavior draft, retained for comparison.
- `aseprite/piplup-draft-v3.aseprite`: earlier 19-frame collar-correction draft.
- `aseprite/piplup-draft-v5.aseprite`: current 64 × 64, 19-frame preferred-face demonstration with six named tags: playback, delay, taking off, neck rest, putting on, resumed playback.
- `previews/piplup-playing-draft-v1.gif`: enlarged playback loop for review, exported with Aseprite. No song-beat synchronization.
- `previews/piplup-headphones-behavior-v5.gif`: current 6× enlarged animation: playing → 3-second delay → headphones to neck → 2-second review hold → headphones on → playing. The real idle state should hold until playback resumes; the GIF loops for review. Earlier previews remain for comparison.
- `previews/piplup-face-review-v5.png`: four native poses enlarged with nearest-neighbor pixels to check the cheek, beak, collar and headset.
- `animation.json`: proposed states and timing, with actual draft frame ranges.
- `ui-palette.json`: UI color targets, independent of the character palette.
- `make-draft-v5.lua`: current Aseprite import/resize/edge-cleanup/timeline script, matching both source strips to a 50-pixel neutral character height and a shared foot baseline. Earlier scripts remain; all refuse to overwrite their existing draft project.
- `PROMPTS.md`: generation prompt record and input roles.

## Next Aseprite pass

1. Review the character silhouette, palette, and window direction before calling anything final.
2. Clean the 64 × 64 sprite with the pencil tool at native resolution: remove faint edge pixels, align the feet, keep the head/headphones consistent, and reduce to a stable 12–16-color palette.
3. Refine the `playing-draft` tag into a smooth repeating head-bob, keeping the closed eye and left-facing beak readable. Clean headset movement and make the head-to-neck transition more gradual; the two intermediate poses are a rough blocking pass.
4. Add charging and low-battery poses only after the base animation is approved; retain left-facing closed eyes and headphones on head or neck as appropriate to playback.
5. Refine the existing 320 × 240 native layouts and test additional playback states, menu scrolling and space around the mascot.
6. Export modified BMPs with `python3 tools/export_piplupos.py`, rebuild and recheck the native parser and GUI before calling a variant ready. The wrapper runs Aseprite and packs the opaque panels as RGB565 so backdrop and sprite backgrounds match.

The generated strip has uneven apparent pixel blocks and frame-to-frame shape differences. Resizing it in Aseprite produces an editable draft, not finished pixel art. The PNG concepts remain illustrations; native prototype packages now exist separately under `dist/themes/`.

## Native work · 2026-10-01

`themes/piplupos/` contains the standard-compatible prototype: complete native menu with a mascot sidebar, playback metadata and controls, light-grey chrome, blue title bars, album cover and playing head-bob. Piplup overlaps the cover window's upper-left edge; animated pool water is the no-cover fallback. The standalone sidebar `pup` label is removed, while the welcome greeting remains. A battery-outline icon drains with the native reported percentage. Pause changes immediately to neck rest. Native menu/file navigation, embedded-JPEG AAC cover display, cover/no-cover track switching, AAC/WAV playback, title scrolling and missing-tag fallbacks were checked through computer use.

`themes/piplupos-delayed/` has a draft playback state machine with a 3-second pause delay, removal poses and return-to-head poses. Normal delay and resume were observed in the modified simulator. It requires HAVE_SKIN_VARIABLES, which stock ipodvideo firmware does not enable. Rapid cancellation, leaving/reentering playback, stop timing, stable 4.0 and device tests remain pending. Its menu mascot uses immediate state changes, separate from the playback timer.

The Mac apps and source patch are described in [SIMULATOR.md](../../docs/SIMULATOR.md). The standard theme is installed on the iPod; the delayed variant remains a custom-firmware prototype. Native renderer captures live in `previews/native-*.png`; they are distinct from the concept boards.

Playback places the mascot canvas at (164, 49), shifted 8 pixels left and 6 pixels up. The 2026-10-02 revision removes the blue strip above the artwork and moves the cover to (196, 66), expanding its maximum area to 103 × 98. The footer shows **Shuffle On / Shuffle Off** from Rockbox's actual shuffle state. Both states were observed after changing the native playback setting. Rodrigo chose normal fixed-speed dancing; BPM synchronization is [no longer planned](beat-sync.md). The skin requests 100 ms poses, but stock 4.0 playback polls at 200 ms, so the faster Mac simulator does not establish hardware cadence.

A small native audio meter below the album name now enables stock Rockbox's 10 Hz peak-meter updates while playing or seeking. The foreground restoration rectangle lives inside each timed pose, so those additional updates restore the previous frame before drawing the next. Pausing removes the meter and disables that extra refresh path. Native Mac playback, pause and resume were checked; actual device frame rate and battery cost remain unmeasured. This is a theme change, with no firmware patch.

The standard skin's WPS and SBS passed the official stable 4.0 parser, and the corrected layout was checked in a stable 4.0 GUI simulator on 2 October 2026. For the physical installation, use [the Mac backup, dual-boot and PiplupOS guide](../../docs/INSTALL_PIPLUPOS_MAC.md) and `dist/themes/piplupos.zip`. Hardware performance still needs retesting; the delayed variant requires custom firmware.

`export-native.lua` batch-loads the 19-frame mascot source and generates editable `aseprite/native-menu.aseprite` and `native-player.aseprite`, plus native BMP assets. Artwork and chrome are drawn onto a cached backdrop with `%VB`; an invisible `nofill,noborder` battery-bar rectangle restores that backdrop before each foreground mascot redraw. The full-screen chrome image uses `%x`, so animation does not repeatedly erase cached artwork. This separates the album-art draw from the sprite draw: Rockbox paints album art after queued images within a viewport. Native Mac tests on 2026-10-02 covered cover/no-cover transitions and pause/resume. Physical verification remains pending. The script regenerates those UI sources, so save manual UI variants elsewhere; it leaves the mascot project untouched.

The main menu and playback window are inset by 9 pixels over an animated pool desktop. Twelve synchronized 0.1-second phases now draw only the exposed top, bottom, left and right strips, leaving the grey controls and artwork intact. The angular water loop has no last-to-first phase jump. `aseprite/native-desktop.aseprite` is the editable twelve-frame pool source. The raised X at the title bar's right edge is visual chrome: this iPod uses Menu/Back, with no touch or mouse close target. The native renderer showed changing border pixels during playback, pause and menu navigation; menu scrolling still reaches Shortcuts. Battery text at 100% fits beside the icon and X. These checks do not establish physical animation cost.

`make-pool-preview.lua` illustrates those border phases over a static native capture in `previews/pool-border-preview.gif`. It is not a simulator recording; playback text and the mascot remain frozen in that asset preview. Regenerate it with Aseprite batch mode, `--script-param capture=design/piplupos/previews/native-playing-layer-fix-2026-10-02.png --script design/piplupos/make-pool-preview.lua`.

Add `--script-param no-cover=1` with the native no-cover PNG to generate `previews/piplupos-motion-preview.gif`, including the faster mascot and pool-window animation. This is a composite asset preview with text held still. The native artist/album names and PiplupOS title are now Helvetica Bold. The converted Rockbox font and its Adobe/DEC permission notice are bundled under `themes/piplupos/fonts/`; the menu and song title retain their regular font.

```sh
python3 tools/export_piplupos.py
python3 tools/modpod.py build piplupos
python3 tools/simulator.py stage piplupos
```

## Stock 4.0 motion correction · 2026-10-02

The playback-state conditional now surrounds the timed pose sequence. A conditional nested inside each timed pose made Rockbox apply its default two-second timeout despite `%t(0.1)`. The corrected sequence advanced every 0.11–0.21 seconds in the stable 4.0 Mac simulator. This is a host measurement; physical cadence and battery cost remain unmeasured. Idle menus still refresh about once per second in stock 4.0. Rodrigo chose to finish this theme update and defer a custom firmware build.

Chrome and artwork now share one full-screen cached viewport. The previous second cache viewport cleared a large rectangle with a different background shade. Opaque UI backdrops and menu mascot sheets are exported as undithered RGB565; the editable Aseprite palette and transparent playback sprite are retained. Native captures show matching panel shades and no overwritten opaque mascot pixels in the sampled playing, paused and no-cover poses. The cache uses font 0 for an internal empty line, which produces a parser warning; visible text uses the bundled fonts and both standard skins parse successfully.

All 19 standard theme files were backed up, copied and checksum-verified on the iPod. The firmware, current settings and all 2,738 audio paths/sizes were preserved. Eject, unplug and reload PiplupOS to activate this revision. Hardware retesting remains pending.

## Feature requirement

Rodrigo wants every original iPod function retained, including Movies, Notes, and Search. A Rockbox skin changes selected interface surfaces; it does not implement Apple's original apps or apply a global mascot overlay to every plugin. See [the preservation matrix](../../docs/FEATURE_PRESERVATION.md). Dual boot was approved on 2026-10-01 and installed on 2026-10-02. Rodrigo's physical photos and feedback establish that PiplupOS starts and music plays; the reported artwork, animation and responsiveness issues need hardware retesting after this revision. Native development and tests use [the Mac simulator workflow](../../docs/SIMULATOR.md).

## Personal touches added on 2026-10-01

Startup should introduce **PiplupOS**, with occasional personal messages using **pup** and **rkzim**. The proposed display/device name is **Piplup's iPod**, editable rather than hard-coded throughout the project. Include a small pixel-art cameo of **Suki's pink Honda S2000**, using Rodrigo's supplied car picture for visual details, not its text or watermarks. Prefer a welcome/about window or occasional scene rather than obscuring track information.

The native theme already uses PiplupOS, pup, rkzim and Piplup's iPod as display text, and animates water/playback. This does not rename the physical iPod. Suki's cameo, a separate welcome scene, charging/low-battery reactions and early boot branding remain pending; preserve track readability and standard menu access when adding them.

Rockbox's early logo is compiled into the firmware because storage is not ready yet (`apps/main.c:show_logo_boot`). A theme alone cannot replace that early screen. A later welcome scene and an optional firmware branding change must be assessed separately; keep normal theme compatibility and dual boot intact.

## Recreate the animation draft

With Aseprite installed, from the repository root:

```sh
/Applications/Aseprite.app/Contents/MacOS/aseprite -b --script design/piplupos/make-draft-v5.lua
```

This intentionally stops if the draft `.aseprite` already exists, so it cannot discard hand edits. Open the saved project in Aseprite to continue. The current project was produced with Aseprite 1.3.18.6-dev.

Official workflow references: [Aseprite animation](https://www.aseprite.org/docs/animation/), [frame tags](https://www.aseprite.org/docs/tags/), [command line](https://www.aseprite.org/docs/cli/), and [Lua API](https://github.com/aseprite/api).
