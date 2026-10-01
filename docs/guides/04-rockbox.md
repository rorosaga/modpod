<!-- Generated from handbook/content.json by tools/modpod.py build. -->
# Install Rockbox

Use the official ipodvideo instructions once the modified hardware works and the iPod is FAT32.

## Before starting

Apple firmware must play music on the new hardware, and the data volume must be FAT32. If it is HFS+, finish the restore/conversion stage first.

## 1. Open the native Mac installer

Rockbox Utility is installed in Applications as a locally compiled Apple Silicon build from official current source. The official 1.5.1 Mac release was Intel-only. Stable Rockbox 4.0 for the 64 MB ipodvideo is prepared locally; see docs/SIMULATOR.md and docs/BUILD_LOG.md. The iPod is still HFS+, so physical installation waits for the FAT32 restore/conversion.

## 2. Select the exact target

Choose iPod Video (ipodvideo), which covers 5th/5.5th generation. Confirm the mount point belongs to your FAT32 iPod. Select the current recommended stable release; record its version and the Utility version in the build log.

## 3. Install bootloader and firmware

Follow Utility’s prompts and the official chapter for the bootloader and Rockbox firmware. Install the fonts package when using themes that require it. Keep power and USB connected until the installer reports completion, then safely eject.

## 4. Test both firmware paths

After the FAT32 restore, resync songs from the Mac using Apple Music. Rockbox can index the same files under iPod_Control/Music without a second copy; load the optional shared-music.cfg and initialize its Database as described in docs/SHARED_MUSIC.md. Test one unprotected song in both firmware paths and check the documented Hold-switch dual boot. Confirm controls, charging and USB before relying on the installation.

## Checklist

- [ ] FAT32 confirmed on the actual iPod
- [ ] Bootloader and current Rockbox firmware installed
- [ ] Rockbox playback and USB test passed
- [ ] Apple firmware dual boot checked; versions logged

## Keep in mind

The manual warns about flash-storage write corruption with Rockbox 3.15 and earlier, fixed in later builds. Use the current recommended release. There is no Rockbox installation on this iPod yet.

## Full references

- [Rockbox iPod Video manual · Installation](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch2.html)
- [Rockbox iPod Video manual · Quick start](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch3.html)
