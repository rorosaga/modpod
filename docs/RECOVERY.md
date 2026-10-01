# If a stage does not work

Stop at the stage that failed; keep the next change out of the diagnosis.

| Symptom | First checks | Reference |
| --- | --- | --- |
| Apple restore fails after the Quad swap | Battery connection, Quad ribbon seating/lock, card in uSD1; then the manufacturer’s card-preparation guide | [iFlash Quad](https://www.iflash.xyz/store/iflash-quad/), [SDXC preparation](https://www.iflash.xyz/prepare-sdxc-exfat-for-use-with-the-ipod/) |
| Case will not close freely | Battery thickness and placement, foam height, cable routing. Do not force it | [Extended battery guide](https://www.iflash.xyz/3rd-party-extended-battery-guide/) |
| Rockbox installer sees an HFS+ iPod | Return to the FAT32/Windows-initialization prerequisite. Verify backup before any restore or conversion | [Official installation chapter](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch2.html) |
| New theme renders badly | Select a known working theme or reset theme settings; check WPS/SBS paths and the native parser result | [Theme manual](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch13.html) |
| Need to start Apple firmware | Follow the manual’s Hold-switch dual-boot sequence. Confirm both firmware paths during installation | [Quick Start](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch3.html) |

The original playback test only proves the stock device could play one song. Do not assume that a later storage, battery, USB, or Rockbox issue is caused by the same earlier Finder problem.

Never disconnect while a restore, firmware installation, or transfer is writing. If a device is stuck, record the screen, host message, and current stage before choosing a reset/eject procedure. Do not reuse a disk number from an earlier connection.
