# PiplupOS · Preserve the iPod's functions

Requirement from Rodrigo: keep **all original iPod functionality**, especially Movies, Notes, and Search. PiplupOS should provide a skin and additions. It is a theme project, not a decision to remove features.

Rodrigo approved dual boot on 2026-10-01. PiplupOS will skin Rockbox; original Apple functions remain accessible by booting Apple firmware. Apple firmware has been restored after the Quad/battery installation, and Rodrigo confirms the new storage capacity. Rockbox is not installed. The confirmed AAC playback baseline predates the hardware swap; post-mod playback still needs testing.

| Requirement | Apple firmware | Rockbox route | What is still needed |
| --- | --- | --- | --- |
| Original Movies experience | Available through original firmware, subject to the restored device/library actually working | MPEG Player supports MPEG-1/2 with MPEG audio in `.mpg`; this is a separate player and format path | Test original movies after the hardware restore; don't promise the same movie files/workflow in Rockbox |
| Original Notes experience | Keep original firmware available | Text Viewer reads text files; Text Editor provides simple editing | Establish whether equivalent text tools satisfy Rodrigo, or original Notes must be used |
| Original Search experience | Keep original firmware available | Rockbox has its own database browsing/search facilities and a playlist Search plugin | Test Rodrigo's actual search needs; don't call it the Apple Search UI |
| Music and click-wheel control | Preserve and retest the known stock playback baseline | Native playback and menu controls can remain while WPS/SBS skins change their appearance | Test both firmware paths, controls, long tags, charging, and USB |
| Animated Piplup mascot | Not implemented by this project in Apple firmware | Native menu/playback prototype with pool/head-bob frames; standard skins pass the stable 4.0 parser; experimental pause timer requires custom firmware | Final sprite cleanup, state edge cases, stable GUI and device performance tests |
| Mascot on every screen | No global overlay implemented | Plugins are separate programs and may draw their own interfaces | Define the exact supported screens; no claim of a mascot over movies/every plugin |

## Approved route: dual boot

### Where the familiar options are

| Option | In Rockbox / PiplupOS | Original Apple experience |
| --- | --- | --- |
| Shuffle all music | Database → Shuffle Songs after indexing the shared files | Apple firmware's Shuffle Songs menu |
| Shuffle the current playlist | Settings → Playback Settings → Shuffle | Apple Settings → Shuffle |
| See the current shuffle state | Playback footer explicitly shows Shuffle On or Shuffle Off from native state | Apple Now Playing shuffle indicator |
| Repeat | Settings → Playback Settings → Repeat | Apple Settings → Repeat |
| Artists, albums and tracks | Database → Artist / Album / Tracks by | Apple Music menu |
| Sound and playback controls | Settings → Sound Settings / Playback Settings | Apple Settings and Now Playing |
| Movies, Photos, Notes and original Search | Separate Rockbox plugins/database tools may provide alternatives | Boot Apple firmware to use the original apps and library databases |

Database → Shuffle Songs and Search, plus Playback Settings → Shuffle and Repeat, were located through the native simulator UI on 2026-10-01. Their absence from the root list does not mean they were removed. The dedicated Database entry provides the all-library shuffle route; the playback setting applies to the current playlist. The actual music library needs checking after the first device index. The skin keeps Rockbox's menu structure rather than recreating Apple's OS menu.

Rockbox can coexist with Apple firmware through the documented dual-boot mechanism. PiplupOS would skin Rockbox's playback/menu surfaces, while booting Apple firmware would provide the original Apple feature experience. Switching firmware means those Apple screens would not automatically gain the PiplupOS skin.

Rodrigo accepts switching firmware for those original features. Preserve both boot paths and test them at installation time. Apple-firmware skin modification has not been assessed or chosen.

A theme alone cannot add arbitrary OS services, mouse-controlled desktop windows, or a system-wide assistant. A timed head-bob during playback works in the native simulator prototype. Actual beat tracking is separate work; do not claim beat synchronization from a repeating frame loop.

The mascot requirement adds a pause/stop delay, lowering headphones to the neck once, holding them there, and putting them back on once when playback resumes. The current Aseprite v5 source specifies those poses. Native simulator checks on 1 October established normal delayed neck rest and resume using a simulator-only HAVE_SKIN_VARIABLES feature. Stock ipodvideo does not enable that feature, so the standard-compatible skin changes immediately on pause. No custom device firmware has been built or installed. Rapid/cross-screen transitions and stopped-state timing remain unverified; see [SIMULATOR.md](SIMULATOR.md).

Apple-synced audio can be indexed separately by Rockbox while sharing the same stored files. See [SHARED_MUSIC.md](SHARED_MUSIC.md) for FAT32/resync prerequisites, supported unprotected files and limits of playlist/artwork sharing.

## Primary sources checked on 2026-09-30

- [Official iPod Video quick start / dual boot](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch3.html)
- [Official plugins chapter: MPEG Player, Search, Text Viewer, Text Editor](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch12.html)
- [Official browsing/database chapter](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch4.html)
- [Official skin configuration: timed sublines](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch13.html)
- [Official skin tags: playback states and BMP sub-images](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildap4.html)

The official manual HTML was fetched directly and read. These are software capabilities, not a claim that the modified iPod or draft theme has been tested.
