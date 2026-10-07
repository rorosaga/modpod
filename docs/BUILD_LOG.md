# Build log

## 2026-09-30 · Apple firmware baseline

- Device reported as an iPod Video with original 80 GB storage and Apple firmware 1.3. Rodrigo identifies it as the 5.5 generation.
- Before modification, the mounted data volume was HFS+ / Mac formatted.
- After a Mac restart and Finder’s Get Started flow, manual music transfer worked.
- One AAC `.m4a` song was copied from the Mac music library. The stored iPod file matched the source hash.
- Rodrigo confirmed that the iPod plays the song. The iPod was safely ejected.
- This establishes a playback baseline. It does not establish long battery runtime, all controls, or flash-storage compatibility.

## Foundation · Local only

- Repository cloned to `Documents/roros_lab/modpod`; branch `setup/project-foundation`.
- Purchases recorded from Rodrigo’s links: iFlash Quad, Amazon Spain Techtek battery, Amazon Spain iFixit toolkit, MediaMarkt SanDisk Ultra PLUS 128 GB card.
- At foundation creation, the hardware swap and Rockbox installation were pending.
- Paper and Midnight remain starter examples with structural checks only.

## 2026-09-30 · Hardware report

- Rodrigo reports completing the iFlash Quad and battery swap, restoring Apple firmware, and seeing the expected new storage capacity.
- Battery pressure on the screen was reported. Physical clearance, charging, closed-case playback and USB reliability remain to be checked; do not infer them from the capacity result.

## 2026-10-01 · Native Mac setup and shared music

- Dual boot approved: Apple firmware retains the original Movies, Notes and Search experience; PiplupOS skins Rockbox.
- Rockbox Utility 1.5.1's official Mac release was Intel-only. A native ARM64 Utility 1.5.2 was compiled from official Rockbox source commit `e45936397ee3677c910c9a0c6473184e9755040c` using Qt 6.11.2, bundled and installed at `/Applications/RockboxUtility.app`. Its executable is ARM64, signature verification passed, and its GUI opened through computer use. This is a local current-source build, not an official released Apple Silicon binary. The installer remains unconfigured; installation has not been started.
- Native ARM64 `ipodvideo` UI simulator built and installed at `/Applications/PiplupOS Simulator.app`. Local host patches and the experimental simulator-only skin-variable feature are recorded in `tools/patches/macos-simulator.patch` and `docs/SIMULATOR.md`.
- Official stable Rockbox 4.0 ZIP downloaded locally and CRC checked. Its target is `ipodvideo`, 64 MB, matching the original 80 GB model. It includes the Helvetica font used by PiplupOS. No firmware or bootloader was copied to the iPod.
- First read-only inspection found the connected 128 GB iPod HFS+ with approximately 11.9 GB used. Subsequent Apple Music sync may increase that figure. Rockbox requires FAT32; no conversion, device reset, ejection, rename or device writes were performed.
- Native database indexing of `iPod_Control/Music/F00/TEST.m4a` passed, including title, artist, album and Apple-style path. Native GUI AAC playback showed the same tags and the 3-minute fixture duration. The test fixture is silent, synthetic audio, not private user music.
- Shared-library settings and first-index/resync instructions are in `design/piplupos/shared-music.cfg` and `docs/SHARED_MUSIC.md`. Physical-song indexing remains pending until a later installation and resync.

## 2026-10-01 · PiplupOS native prototype

- Editable mascot remains `design/piplupos/aseprite/piplup-draft-v5.aseprite`: 64 × 64, 19 frames. Aseprite exported native menu/player backdrops, pool animation and opaque composite sprite strips. Editable generated UI sources are stored beside the mascot.
- Native WPS and SBS parsing passed for both `piplupos` and `piplupos-delayed` using `checkwps.ipodvideo` at the recorded development commit. Standard-theme full menu navigation, file browsing, AAC/WAV playback, pause, title scrolling, missing artist/album fallbacks and pool/mascot rendering were verified through computer use.
- The stock-compatible theme uses timed head-bob/water frames and immediate neck rest when paused. The experimental WPS showed headphones on during its pause delay, at the neck after the delay, and back on after resume. This needs HAVE_SKIN_VARIABLES, which stock ipodvideo firmware does not enable. Only the simulator has been built with that feature.
- An animation redraw artifact was corrected using opaque pool/sprite composites; a tiny nonprinting control viewport prevents title erasure. All standard menu entries remain accessible, with a separate mascot sidebar.
- Native 320 × 240 renders are in `design/piplupos/previews/native-*-2026-10-01.png`; these are renderer output, not browser illustrations.
- The local handbook now opens PiplupOS by default and includes both native menu/playback captures. Its updated status and theme workshop layout were reviewed in the in-app browser; the palette editor remains a clearly labeled generic illustration.
- Seven focused package/path-safety tests pass. Native checks above do not certify stable Rockbox 4.0 or device performance.
- Still pending: quick pause/resume cancellation, cross-screen state persistence, stopped-state timing, shuffle/repeat/seek edge cases, final pixel cleanup, Suki cameo, early boot logo, and physical dual-boot/playback/storage/battery checks.
- Everything remains local on `setup/project-foundation`; no commit, push or merge.

## 2026-10-01 · Cover-art layout revision

- Removed the standalone `pup` sidebar label requested by Rodrigo; retained `Welcome back, pup.` and `rkzim`.
- The existing playback window now shows native album art, constrained to 103 × 84 with aspect ratio preserved. The 64 × 64 mascot canvas overlaps the window's upper-left corner at (179, 48). Artist/album text width was reduced slightly to prevent overlap.
- Songs without a usable cover show animated pool water. A synthetic M4A with embedded baseline JPEG artwork verified the cover path; switching to the unillustrated AAC fixture verified fallback and removal of old artwork.
- A battery outline is embedded in both Aseprite UI backdrops. Native `%bl` draws the fill alongside the percentage. Simulated charge levels from nearly full through zero showed the corresponding fill changes; this does not measure the physical replacement battery.
- An initial overlay prototype erased a rectangle of the cover on pause. The final single viewport redraws art/water with timed pose updates and uses an Aseprite-exported underlay outside the art region. Standard pause/resume and normal experimental delayed neck/rest/resume were rechecked over artwork without that artifact.
- Both native skin pairs pass parser checks, and the focused package/path checks pass. Full native captures were updated in the theme workshop.
- The actual Database menu contains Album Artist, Artist, Album, Genre, Year, Composer, Tracks by, Shuffle Songs and Search. Playback Settings also retains Shuffle and Repeat. `docs/FEATURE_PRESERVATION.md` now maps these locations to the familiar Apple options.
- No real iPod data or firmware was changed; nothing pushed.

## 2026-10-01 · Animated pool desktop

- Inset both menu and playback windows to (9, 9), 302 × 222. Water now forms an animated 9-pixel desktop border around the grey window, with a raised X on its title bar. X is visual chrome on the click-wheel target; normal Menu/Back navigation remains the action.
- Added editable four-frame `native-desktop.aseprite` and four synchronized strip sheets. Only exposed strips redraw every 0.2 seconds; the sheets contain 39,024 pixels total rather than a 307,200-pixel full-screen four-frame sheet. Actual device CPU/memory and battery cost remain unmeasured.
- Native GUI checked menu scrolling through Shortcuts, nested settings, standard pause/resume, cover/no-cover track changes and the experimental normal headphone delay/resume. The battery icon and 100% text fit beside X. Both variants parse and all seven package/path checks pass.
- Two native F5 playback dumps showed 2,810 changed pixel-data bytes in the top border, confirming real renderer animation. Updated native previews are retained with the project. The optional GIF previews the border phases over a native capture, rather than recording simulator playback.
- No physical iPod writes, commits or pushes.

## 2026-10-01 · Smoother motion and bold metadata

- Changed native animation sublines from 200 ms to 100 ms. Generated 12 water phases with a full angular cycle, removing the old four-frame loop's abrupt wrap. The faster Aseprite timing revision preserves all v5 pixel artwork; the previous project remains intact.
- Stock idle menu waits can be one second and playback waits 200 ms. The Mac-only simulator patch caps those waits at 50 ms, reduces its menu update delay and avoids a missed alternator deadline at tick equality. The native animation target is nominally 10 frames/s; no frame-rate benchmark or physical-device performance claim is made.
- Rebuilt the native ARM64 simulator, refreshed its virtual theme/font files and verified its app signature. Native GUI checked bold title/artist/album text, standard pause/resume, cover/no-cover switching, animated menus and the experimental normal headphone delay and resume. No new pixel trails or artwork-erasure artifact appeared.
- Bundled the official Rockbox Adobe Helvetica Bold conversion and its permission notice. The package and safe local staging helpers support RB12 fonts; variant-copy coverage and invalid/symlink-font rejection pass. All eight focused tests and all four skin parser checks pass.
- Refreshed native handbook captures plus 100 ms asset-preview GIFs. The composite motion GIF freezes playback text while illustrating exported water/mascot frames; it is not a native playback recording.
- No real iPod data/firmware changes and no commits or pushes.

## 2026-10-01 · Mascot placement, shuffle state and publication

- Moved the playback mascot canvas from (172, 55) to (164, 49): 8 pixels left, 6 pixels up. Album art stays at (196, 80); the shared viewport, exported underlay and composite preview use the same offsets. Left metadata widths keep text clear of the mascot.
- Both playback skins now explicitly display Shuffle On or Shuffle Off through native `%ps`. Changed Shuffle from Yes to No in the native playback settings and observed the footer update while playing; retained an Off capture alongside the cover and no-cover previews.
- Native GUI checked the new position with cover art, no-cover water, normal delayed neck rest and resumed playback. All eight focused tests and all four WPS/SBS parser checks pass. Mac simulator checks remain separate from physical-device validation.
- Recorded a proposed offline-analysis/custom-firmware beat-sync approach in `design/piplupos/beat-sync.md`. The current loop is fixed timing; no BPM analyzer or beat clock has been implemented.
- Rodrigo authorized publishing the project through a dev branch, PR to main and merge. The repository had no commits or remote branches; an empty main commit provides the PR base. Local Rockbox builds, virtual storage/music, downloaded firmware, generated packages and private/reference images remain excluded.
- No physical iPod data or firmware changes were performed.

## 2026-10-01 · Fixed dance speed confirmed

- Rodrigo chose normal fixed-speed dancing. Retained the existing 100 ms playing poses and pause/headphone behavior; no skin or asset changes were needed.
- Removed BPM synchronization from planned work and replaced its proposal with the decision record. No beat-analysis or custom beat-clock implementation will be pursued under the current scope.

## 2026-10-01 · Stable parser and Mac installation guide

- Official live build information still lists Rockbox 4.0 as the stable ipodvideo release. The prepared official ZIP identifies ipodvideo, 64 MB, version 4.0 and includes the regular Helvetica font used by PiplupOS.
- Built the native checkwps tool from official `v4.0-final`, commit `e094c599fa60236527f9e272e0b8309d7696e399`. Used installed GCC 16 instead of the configure script's hardcoded GCC 14 host tools and generated language headers before compilation; skin parser and target feature definitions remain unchanged. Both current standard PiplupOS WPS/SBS parse successfully. This is not a stable GUI or hardware test.
- Rodrigo only has his M4 Pro Mac and wants to preserve songs already synced to the iPod. Added `docs/INSTALL_PIPLUPOS_MAC.md` with hidden iPod_Control backup/recovery, the remaining disk-layout check, Utility installation, iPod Video dual boot, standard theme ZIP merge, and shared music indexing. No song backup is claimed complete.
- A fresh `diskutil list external physical` check returned no devices. The first HFS+ observation remains historical; current filesystem, capacity, sector size and disk identifiers require a connected-device inspection.
- Built official-source ipodpatcher from commit `e45936397ee3677c910c9a0c6473184e9755040c`; verified native ARM64 output and its help. No embedded bootloader/default installation mode was built. Upstream's experimental conversion and formatting routines only support 512-byte sectors. The historical Mac reference covers 2048-byte-sector Video models, but its stock 80 GB partition map is not verified for this 128 GB modification. No formatting command is prescribed until the actual layout is checked.
- No physical iPod writes, conversion, firmware installation, resets or disconnections occurred. Local downloaded source, tool binaries, firmware and any future private music backup remain excluded from Git.

## 2026-10-02 · Physical feedback and theme/library fixes

- Rodrigo supplied physical PiplupOS photos and reported successful Apple/Rockbox dual boot and music playback. Reports include changing battery estimates after reboot, a database scan counter near 2,788, slow animation, artwork clipping the mascot, greyscale covers and delayed rapid skipping while the previous audio continues. A later read-only device check confirmed the database had completed: 2,738 committed entries, no dirty/deleted entries, and every indexed path matching installed music. Battery runtime remains unverified; these symptoms do not establish a failing battery or storage card.
- Removed the blue strip above artwork and enlarged its area from 103 × 84 to 103 × 98 at (196, 66). Piplup remains at (164, 49). A cached `%VB` backdrop separates the album-art and foreground image draws. Static `%x` draws the chrome, a full foreground viewport copies it on full redraws, and an invisible restoration rectangle inside each timed pose clears previous sprite pixels. This avoids the renderer's album-art-after-images draw order in one viewport.
- Added a small playing/seek audio meter using the stock 10 Hz peak-meter refresh route. It disappears and disables that extra route on pause. Native Mac cover/no-cover transitions, coloured fixture covers, real M4A playback, pause/resume and menu return were checked. The stock skin parser accepts the standard theme; physical frame rate, battery cost and rapid-skip performance still need retesting.
- Reproduced greyscale artwork for the original colour Currents JPEG in the Mac simulator. A screen-sized uncompressed RGB BMP displayed the correct colours without changing audio. Prepared 1,277 private album-cover files (37,111,718 bytes) from Mac originals; one case-variant album key with conflicting artwork retained its first cover. The optional device-fixes preset prefers image files and uses song titles in playlist views. The precise JPEG-decoder cause remains unresolved.
- Verified the reported playlist's first four-letter entry maps to a real song. The native playlist viewer displayed tagged song titles with `playlist viewer track display: title from tags`; included that setting in the optional library preset. No rescan is required for this display setting.
- Downloaded the official Rockbox Doom data ZIP. The device already contained its support WAD and both Freedoom WADs; stock 4.0 requires the recognised name `doomf.wad`. Added a verified copy of Freedoom 2 under that name. The native ARM64 simulator detects it and opens the Doom menu, but gameplay crashes with a bus error. Physical gameplay is pending; no commercial game data was downloaded. See [GAMES.md](GAMES.md).
- Native framebuffer comparisons found zero mismatched opaque mascot pixels, allowing for RGB565 quantisation, in the captured playing and neck-rest poses. All eight focused tests passed, along with project validation/build and the stable standard WPS/SBS parser checks. These checks do not establish every frame or physical performance.
- On reconnect, verified the same FAT32 volume UUID and stock 4.0 target, backed up existing theme/settings files, and copied the update. SHA256 verification passed for all 19 stock theme files, 1,277 colour covers, Doom game/support WADs and the settings preset. All 2,738 audio paths and sizes were unchanged; config.cfg, config.cfg.new and config.cfg.old were preserved. After ejecting, load the root `piplupos-device-fixes.cfg` and reload PiplupOS. Hardware animation, skipping, colour and Doom gameplay retests remain pending.
- Local work remains on `dev/piplupos-render-fix`. No bootloader changes, formatting, resets, commits, pushes or merges were performed in this revision.

## 2026-10-02 · Stock motion timing and panel correction

- Reproduced the two-second playing pose timeout in the stable 4.0 renderer. Nested state conditionals overrode the explicit 100 ms pose time. Moved the state selection outside the timed sequence; stable simulator measurements show 0.11–0.21 seconds between playing poses. Idle stock menus remain about one update per second. Rodrigo deferred the proposed custom firmware build and requested this theme fix first.
- Combined artwork and chrome in one cached backdrop viewport, removing the large pale rectangle and retaining the enlarged artwork bevel. Exported opaque UI panels/menu mascot sheets as undithered RGB565 through `tools/export_piplupos.py`; the editable palette and transparent playback sheet are unchanged. Playing, pause, no-cover and menu captures have matching panel shades; sampled opaque playing/neck-rest sprite pixels have zero mismatches within native RGB565 quantisation.
- Built an isolated GUI simulator from official `v4.0-final` with SDL threads, host input-tap support and timing diagnostics. No animation scheduling patch or skin-variable feature is enabled in that release simulator. Both standard skins parse successfully; the internal font-0 cache viewport produces a warning. All eight focused tests and project validation pass.
- Reverified the physical FAT32 volume UUID and stock 4.0 ipodvideo/64 MB target. Backed up and copied all 19 standard theme files, then verified SHA256 hashes. All 2,738 audio paths/sizes, current settings and firmware hashes are preserved. Theme reload and physical animation/background retest are pending. No custom firmware, bootloader changes, formatting, commits or publication occurred.

## Hardware session · To fill in

- Date / before photo:
- Back-shell measurement:
- Battery label and measured dimensions:
- Card manufacturer SKU:
- Quad / ribbon / card-slot photo:
- Dry-fit clearance result:
- Apple restore method / filesystem / reported capacity:
- Playback / controls / charging / USB test:
- Closed-case result:

## Rockbox session · To fill in

- Backup complete:
- Confirmed FAT32 volume:
- Rockbox Utility version and host OS:
- Bootloader / Rockbox build installed:
- Apple dual boot and Rockbox playback:
- Theme / simulator / device findings:
