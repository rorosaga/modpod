# One music library in Apple firmware and Rockbox

Continue syncing ordinary audio files with Apple Music while booted into Apple firmware. Apple stores synced files under `/iPod_Control/Music/Fxx/`, with renamed filenames. Rockbox reads the audio files and their embedded metadata, and builds its own Database for artist, album and title browsing. A second copy of every song is unnecessary.

The 2026-10-02 hardware session converted the device to FAT32, installed stock Rockbox 4.0 with Apple dual boot, and resynced the Mac library. Later photos and feedback show PiplupOS running and music playing. A read-only inspection confirmed a clean committed database containing all 2,738 songs; every indexed path exists and matches the installed music set. No database rebuild is needed for the current library. Keep the Mac originals; theme, playlist-display and plugin-data updates do not require another conversion. See [the Mac installation and backup guide](INSTALL_PIPLUPOS_MAC.md) for installation/recovery reference.

For the initial library setup:

1. Load the optional `design/piplupos/shared-music.cfg` settings file in Rockbox. It selects `/iPod_Control/Music` and `/Music` for recursive scanning and enables automatic database updates at boot. Keep this separate from theme selection so changing the skin does not change library settings.
2. Use **Settings → General Settings → Database → Initialize Now** for the first index only. Let it finish; Rockbox may request a restart to commit the first database.
3. Browse **Database → Artist / Album / Track**. The Database shows embedded tags instead of Apple's short filenames. Files with missing tags need metadata repair on the Mac and a resync.
4. After future Apple syncs, boot Rockbox and let Auto Update complete, or use **Update Now**. Update Now preserves Rockbox play counts and ratings; Initialize Now rebuilds them.

Apple's playlists, ratings and iTunes artwork database are separate from Rockbox's. Matching song availability does not imply automatic playlist/artwork migration. DRM-protected subscription downloads are not ordinary playable AAC files. Rockbox supports unprotected AAC/M4A, ALAC and MP3, among other formats.

## Playlist entries show four-letter names

Apple stores songs under names such as `LZFA.m4a`. This does not mean the song is missing: the inspected first entry in Rodrigo's `01 - i miss u.` playlist points to Snoop Dogg's **Let's Get Blown**. Choose **Settings → General Settings → Playlists → Playlist Viewer Settings → Track Display → Title from ID3 tags**. The persisted configuration value is `playlist viewer track display: title from tags`, also included in the optional shared-music preset. No database rebuild is needed for this display setting. A native Mac playlist test displayed embedded song titles rather than storage names.

## Album covers in PiplupOS

The playback window displays available album art, preserving aspect ratio within 103 × 98 pixels. The blue strip above the artwork was removed on 2026-10-02. Piplup overlaps its upper-left corner; an animated pool appears when no usable cover is found.

Rockbox can read supported embedded JPEG artwork in MP4/M4A and ID3v2 tags. For external images, use a baseline JPEG or uncompressed BMP beside the track, such as `filename.jpg` or `cover.jpg`. For Apple's scattered `Fxx` storage layout, a separate `/.rockbox/albumart/Album Artist-Album Title.jpg` collection is convenient; Rockbox falls back to Artist when Album Artist is absent. Unsupported filename characters need the replacements listed in the official album-art reference. A generic `cover.jpg` in an Apple `Fxx` folder would apply to unrelated tracks, so avoid that shortcut.

Artwork visible in Apple Music is not proof of supported artwork inside the synced audio file. Apple's separate artwork database is not used by this skin; those covers may need an export. Embedded PNG and progressive JPEG do not satisfy the documented JPEG path. Check representative real files after installation instead of claiming the whole library already has covers.

### Colour-cover workaround · 2026-10-02

Rodrigo reported greyscale covers on hardware. The native Mac simulator reproduced greyscale rendering from the original embedded colour JPEG in **New Person, Same Old Mistakes**, while a smaller synthetic embedded JPEG remained coloured. The exact decoder cause has not been established. A separate uncompressed RGB BMP, resized to fit the theme's artwork area, displayed the original colours correctly. Audio files were unchanged.

Private BMP exports from the existing Mac music files are prepared under ignored `local/diagnostics/2026-10-02-theme/cover-cache/.rockbox/albumart/`. Their names use the file's Album Artist (or Artist) and Album tags, Rockbox's unsupported-character replacements, and the `.103x98.bmp` size suffix. All 1,277 unique covers, totalling 37,111,718 bytes, were copied to the device and SHA256-verified on 2026-10-02. One album-name case variation had conflicting images and retained the first cover instead of overwriting it. Covers and music stay excluded from Git.

For later updates, copy the prepared cover files into the iPod's `/.rockbox/albumart/`, then select **Settings → Playback Settings → Album Art → Prefer image file**. The current files are already installed. After safely ejecting and disconnecting, open **Files → piplupos-device-fixes.cfg** to apply both cover preference and playlist titles; its source is [device-fixes.cfg](../design/piplupos/device-fixes.cfg). Reload **Settings → Theme Settings → Browse Theme Files → PiplupOS** to activate the revised layout. Existing settings files were backed up and preserved. Embedded artwork remains the fallback. This reduces image decoding work, but hardware colour and rapid-skip responsiveness remain to be retested.

## Now Playing controls

Rockbox's default iPod controls differ from Apple's Select-cycle: rotate the wheel for volume, hold Previous/Next to seek, and hold Center for the track context menu. A short Center press opens the file browser. PiplupOS changes the skin; it does not remap these buttons. [Official iPod keymap](https://github.com/Rockbox/rockbox/blob/master/apps/keymaps/keymap-ipod.c).

## Local verification · 2026-10-01

The official Rockbox `ipodvideo` desktop database tool indexed a silent tagged AAC fixture at `iPod_Control/Music/F00/TEST.m4a` in the project's simulated disk. Its native `.tcd` database contained the fixture's artist, album, title and Apple-style path. The native GUI also decoded and played the AAC file and displayed its correct artist, album, title and duration. This establishes the scan/metadata/playback route; it does not establish that every song currently syncing to the physical iPod has been indexed or played. No user music was needed for the test.

An additional silent M4A fixture containing an embedded baseline JPEG was decoded and displayed by the native theme. Switching to the fixture without a cover produced the animated-pool fallback, with no previous cover retained. The standard pause pose and resumed playing pose preserved the cover underneath.

The Mac/utility and simulator setup is documented in [SIMULATOR.md](SIMULATOR.md). No physical iPod data was modified for these tests.

Primary references: [Rockbox database manual source](https://github.com/Rockbox/rockbox/blob/master/manual/rockbox_interface/tagcache.tex), [default database scan settings](https://github.com/Rockbox/rockbox/blob/master/apps/settings_list.c), [supported audio formats](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/file_formats.tex), [album-art requirements and search order](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/album_art_info.tex).
