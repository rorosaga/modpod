# One music library in Apple firmware and Rockbox

Continue syncing ordinary audio files with Apple Music while booted into Apple firmware. Apple stores synced files under `/iPod_Control/Music/Fxx/`, with renamed filenames. Rockbox reads the audio files and their embedded metadata, and builds its own Database for artist, album and title browsing. A second copy of every song is unnecessary.

The current iPod is HFS+; Rockbox cannot yet run on it. Keep the Mac originals. A later FAT32 conversion may erase the iPod and require a restore/resync. Do not perform that conversion during an active sync.

After the eventual dual-boot installation and music resync:

1. Load the optional `design/piplupos/shared-music.cfg` settings file in Rockbox. It selects `/iPod_Control/Music` and `/Music` for recursive scanning and enables automatic database updates at boot. Keep this separate from theme selection so changing the skin does not change library settings.
2. Use **Settings → General Settings → Database → Initialize Now** for the first index only. Let it finish; Rockbox may request a restart to commit the first database.
3. Browse **Database → Artist / Album / Track**. The Database shows embedded tags instead of Apple's short filenames. Files with missing tags need metadata repair on the Mac and a resync.
4. After future Apple syncs, boot Rockbox and let Auto Update complete, or use **Update Now**. Update Now preserves Rockbox play counts and ratings; Initialize Now rebuilds them.

Apple's playlists, ratings and iTunes artwork database are separate from Rockbox's. Matching song availability does not imply automatic playlist/artwork migration. DRM-protected subscription downloads are not ordinary playable AAC files. Rockbox supports unprotected AAC/M4A, ALAC and MP3, among other formats.

## Album covers in PiplupOS

The playback window now displays available album art, preserving aspect ratio within 103 × 84 pixels. Piplup overlaps its upper-left corner; an animated pool appears when no usable cover is found.

Rockbox can read supported embedded JPEG artwork in MP4/M4A and ID3v2 tags. For external images, use a baseline JPEG or uncompressed BMP beside the track, such as `filename.jpg` or `cover.jpg`. For Apple's scattered `Fxx` storage layout, a separate `/.rockbox/albumart/Album Artist-Album Title.jpg` collection is convenient; Rockbox falls back to Artist when Album Artist is absent. Unsupported filename characters need the replacements listed in the official album-art reference. A generic `cover.jpg` in an Apple `Fxx` folder would apply to unrelated tracks, so avoid that shortcut.

Artwork visible in Apple Music is not proof of supported artwork inside the synced audio file. Apple's separate artwork database is not used by this skin; those covers may need an export. Embedded PNG and progressive JPEG do not satisfy the documented JPEG path. Check representative real files after installation instead of claiming the whole library already has covers.

## Local verification · 2026-10-01

The official Rockbox `ipodvideo` desktop database tool indexed a silent tagged AAC fixture at `iPod_Control/Music/F00/TEST.m4a` in the project's simulated disk. Its native `.tcd` database contained the fixture's artist, album, title and Apple-style path. The native GUI also decoded and played the AAC file and displayed its correct artist, album, title and duration. This establishes the scan/metadata/playback route; it does not establish that every song currently syncing to the physical iPod has been indexed or played. No user music was needed for the test.

An additional silent M4A fixture containing an embedded baseline JPEG was decoded and displayed by the native theme. Switching to the fixture without a cover produced the animated-pool fallback, with no previous cover retained. The standard pause pose and resumed playing pose preserved the cover underneath.

The Mac/utility and simulator setup is documented in [SIMULATOR.md](SIMULATOR.md). No physical iPod data was modified for these tests.

Primary references: [Rockbox database manual source](https://github.com/Rockbox/rockbox/blob/master/manual/rockbox_interface/tagcache.tex), [default database scan settings](https://github.com/Rockbox/rockbox/blob/master/apps/settings_list.c), [supported audio formats](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/file_formats.tex), [album-art requirements and search order](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/album_art_info.tex).
