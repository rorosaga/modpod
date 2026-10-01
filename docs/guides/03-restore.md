<!-- Generated from handbook/content.json by tools/modpod.py build. -->
# Restore & test Apple firmware

Prove that the new hardware works before introducing Rockbox.

## Before starting

The Quad, card, and battery should be seated correctly, with no pressure on the cell or cables. Have your backup available.

## 1. Restore the new storage

Use Apple’s supported iPod restore flow for the connected device. This erases the new storage. Confirm the selected device is your iPod. If restore fails, use the iFlash card-preparation reference and recheck seating before trying again.

## 2. Plan FAT32 before Rockbox

Rockbox requires FAT32 with the appropriate iPod firmware/partition layout. A Mac restore may produce HFS+ again. Rodrigo only has an M4 Pro Mac: use docs/INSTALL_PIPLUPOS_MAC.md for backup and the remaining live disk-layout check. The official Mac conversion reference uses old stock-capacity tables; do not blindly apply the 80 GB table to this 128 GB mod. The built-in experimental converter supports only 512-byte sectors. Verify the actual sector size and boundaries before choosing a conversion method.

## 3. Transfer one known song

Repeat the Apple-firmware music test with the same AAC song. Safely eject, then confirm playback, track navigation, headphone output, charging, and USB reconnection.

## 4. Record and close

Record reported capacity, filesystem, and results in the build log. After the open-case checks pass, close without force and repeat the basic playback and charging checks.

## Checklist

- [ ] Apple restore completed on new storage
- [ ] Playback, controls, charging, and USB tested
- [ ] Actual filesystem and reported capacity recorded
- [ ] Case closes freely; closed-case test passed

## Keep in mind

Formatting and restoration erase storage, but a verified Mac copy can preserve the songs. The conversion session needs the current device identity, sector size, partition map and backup checked. No project script performs these operations.

## Full references

- [iFlash Quad · Product and illustrated installation](https://www.iflash.xyz/store/iflash-quad/)
- [iFlash · SDXC preparation and troubleshooting](https://www.iflash.xyz/prepare-sdxc-exfat-for-use-with-the-ipod/)
- [Rockbox iPod Video manual · Installation](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch2.html)
