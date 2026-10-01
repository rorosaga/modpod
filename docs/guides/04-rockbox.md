<!-- Generated from handbook/content.json by tools/modpod.py build. -->
# Install Rockbox

Use the official ipodvideo instructions once the modified hardware works and the iPod is FAT32.

## Before starting

Apple firmware must play music on the new hardware, and the data volume must be FAT32. If it is HFS+, finish the restore/conversion stage first.

## 1. Open the native Mac installer

Rockbox Utility is installed in Applications as a locally compiled Apple Silicon build from official source. The official 1.5.1 Mac release was Intel-only. Stable Rockbox 4.0 for the 64 MB ipodvideo is prepared locally and remains the stable release in official build information checked on 1 October 2026. See docs/INSTALL_PIPLUPOS_MAC.md. The last device inspection found HFS+; no iPod was mounted at the latest check. Physical installation has not started.

## 2. Select the exact target

Choose iPod Video (ipodvideo), which covers 5th/5.5th generation, and the 64 MB variant if prompted: the original 80 GB model determines RAM, not the upgraded storage. Confirm the mount point belongs to the verified FAT32 iPod. Select stable 4.0 and record the firmware and Utility versions in the build log.

## 3. Install bootloader and firmware

Follow Utility’s prompts and the official chapter for the bootloader and Rockbox firmware. Install the fonts package when using themes that require it. Keep power and USB connected until the installer reports completion, then safely eject.

## 4. Test both firmware paths

Use the exact Hold-switch dual-boot steps in docs/INSTALL_PIPLUPOS_MAC.md. Apple firmware retains original Movies, Notes and Search. Resync songs from the Mac originals or verified iPod backup using Music while booted into Apple firmware. Rockbox can index those same files under iPod_Control/Music without a second copy; load shared-music.cfg and initialize its Database as described in docs/SHARED_MUSIC.md. Test one unprotected song in both firmware paths, plus controls, charging and USB.

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
- [Rockbox · Mac iPod conversion to FAT32](https://www.rockbox.org/wiki/IpodConversionToFAT32)
