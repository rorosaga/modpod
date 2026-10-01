# Rockbox + PiplupOS on Rodrigo's Mac

For the iPod Video **5.5 generation**, originally 80 GB, now using an iFlash Quad and a 128 GB card. Rockbox target: **ipodvideo, 64 MB**. The increased storage does not change its RAM or make it an iPod Classic target.

**Start with a music backup.** The last connected-device inspection found HFS+. No iPod is mounted at this guide's final check on 1 October 2026, so its current format, disk identifier and sector size still need a fresh inspection. No formatting or physical Rockbox installation has been performed.

## 1. Keep the songs already on the iPod

You do not need to download the songs again if their audio files can be copied and verified first. HFS+ → FAT32 conversion erases the data volume; the files cannot remain in place during this procedure.

1. Finish the current Apple Music/Finder sync. Keep any existing song originals on the Mac.
2. Connect the iPod and open its **storage volume** in Finder. If needed, enable disk use in the iPod's Finder settings. Do not choose Restore or Erase.
3. Press **Command–Shift–.** to show hidden files. Copy the entire **iPod_Control** folder into a new folder on the Mac, for example `~/Music/iPod-backup-2026-10-01/`. Copy any other files worth keeping, including Notes and personal files. Use Copy/Paste so the originals stay on the iPod.
4. Apple-synced audio is inside the backup's **iPod_Control/Music/F00, F01…** folders. Its short, scrambled filenames are normal; the audio usually retains title/artist/album tags. Videos may also be stored in this tree.
5. Compare the original and copied folder's file counts and byte sizes. Play several copied songs directly from the Mac backup. A complete installation session should also verify checksums of all copied files before erasing anything. Keep sufficient free Mac storage for the full backup.

Copying all of iPod_Control also preserves the available Apple library metadata and artwork files. This guide does not promise that copying that database back will restore every playlist, rating or Apple artwork entry. The dependable Apple-library route is to import the backed-up audio into Music on the Mac and sync it again. Rockbox can play copied, unprotected audio directly.

Apple's renamed/hidden storage and Rockbox's Database route are described in the [official installation manual](https://github.com/Rockbox/rockbox/blob/master/manual/getting_started/installation.tex). See [shared music and album art](SHARED_MUSIC.md).

## 2. Check the format before changing anything

**FAT32** is a filesystem: the way a drive organizes its files. macOS can read and write it. Disk Utility calls it **MS-DOS (FAT)**; inspect the detailed information to confirm **FAT32**, rather than FAT16 or exFAT. Rockbox on this iPod needs a FAT32 data partition and the appropriate iPod firmware/partition layout.

Open Disk Utility, choose **View → Show All Devices**, and identify the external iPod by its name, capacity and USB connection. Record the physical device and its data partition. These Terminal commands only inspect disks:

```sh
diskutil list external physical
diskutil info /dev/diskN
diskutil info /dev/diskNsM
```

`diskN` and `diskNsM` are placeholders, not commands to paste unchanged. Use the identifiers just verified for this iPod. They can change on every connection. Never guess a disk number.

- If it already has the normal iPod DOS/MBR layout and a FAT32 data volume, preserve the songs and continue to section 3. A normal Rockbox installation does not require erasing that data volume.
- If it is HFS+, finish and verify the backup before a separate conversion session. Erasing the whole device in Disk Utility would remove the firmware partition needed for Apple dual boot.

### Mac-only conversion needs one more device check

Windows access is not required for the Mac preparation or subsequent music use. The official [Mac conversion reference](https://www.rockbox.org/wiki/IpodConversionToFAT32) describes a manual route, including 2048-byte-sector Video models. Its supplied partition tables are for original stock disk capacities; **do not blindly apply its stock 80 GB table to this modified 128 GB iPod**.

A native ARM64 `ipodpatcher` was built locally from official source at:

```text
/Users/rorosaga/Documents/roros_lab/modpod/local/rockbox/source/utils/ipodpatcher/ipodpatcher
```

During the conversion session, first inspect the verified device with its read-only `--list` action, and save the partition map and Apple firmware partition to the Mac. This tool's `--read-partition` action makes a firmware-partition backup; it does not back up the songs. Administrator access may be needed to read the raw device. If macOS requires unmounting for raw access, use Unmount after the sync/backup finishes, rather than Eject.

The tool offers `--convert`, but upstream explicitly calls it **experimental**, erases data, and restricts both its partition-table writer and FAT32 formatter to **512-byte sectors**. A successful build/help check is not a device conversion test. No conversion command is prescribed here until the actual sector size and modified partition boundaries have been checked. For 2048-byte sectors, prepare the manual route from this device's real layout; do not disable the tool's guards. See the pinned [conversion source](https://github.com/Rockbox/rockbox/blob/e45936397ee3677c910c9a0c6473184e9755040c/utils/ipodpatcher/main.c), [partition-table writer](https://github.com/Rockbox/rockbox/blob/e45936397ee3677c910c9a0c6473184e9755040c/utils/ipodpatcher/ipodpatcher.c) and [formatter](https://github.com/Rockbox/rockbox/blob/e45936397ee3677c910c9a0c6473184e9755040c/utils/ipodpatcher/fat32format.c).

After conversion, inspect the resulting partition layout, FAT32 volume and full reported capacity, then verify that Apple firmware starts. Treat error output as failure even if a tool exits with status zero. A new Restore on the Mac may produce HFS+ again; if Finder asks for another restore, stop and inspect before accepting it.

## 3. Install Rockbox with Apple dual boot

Proceed only after the FAT32 and Apple-firmware checks above pass.

1. Open **Applications → RockboxUtility**. The installed app is a locally compiled, native Apple Silicon Utility 1.5.2, rather than an official released ARM download.
2. Open its configuration and use **Autodetect**. Confirm **iPod Video / ipodvideo**, the actual iPod mount point, and the **64 MB** variant if asked. Avoid the sixth-generation iPod Classic target.
3. Select **stable Rockbox 4.0**, verified against official build information on 1 October 2026. Choose the **bootloader, Rockbox firmware and fonts**. Save any bootloader backup the installer offers on the Mac. Follow its permission prompts and wait for successful completion.
4. Safely eject and disconnect when the installer instructs you. These physical steps cannot be completed while keeping the iPod continuously connected.
5. Check both boot paths and play one known unprotected song before copying a large library.

The prepared official firmware ZIP is `local/rockbox/rockbox-ipodvideo-4.0.zip`; Utility is the preferred installer. Never use the Mac simulator's firmware or virtual `.rockbox` folder on the physical iPod. References: [official installation chapter](https://download.rockbox.org/daily/manual/rockbox-ipodvideo/rockbox-buildch2.html), [live build versions](https://download.rockbox.org/build-info).

### Switching between Apple and Rockbox

- **Apple firmware:** with the iPod off, turn it on and immediately switch **Hold ON** until Apple firmware starts. Then release Hold to use the controls. The manual also documents starting Apple firmware by connecting USB with Hold already ON.
- **Rockbox:** leave **Hold OFF** at startup. To return from Apple firmware, hold **Menu + Center** until the iPod resets, keeping Hold OFF.
- Sync with Music/Finder while running Apple firmware. Apple provides the original Movies, Notes, Photos and Search experience. PiplupOS changes Rockbox's appearance.

These are the iPod Video instructions, not the different Classic boot controls. [Official dual-boot reference](https://github.com/Rockbox/rockbox/blob/master/manual/rockbox_interface/main.tex).

## 4. Install this PiplupOS theme

Use **piplupos.zip** for stock 4.0. The `piplupos-delayed` variant requires custom firmware and is not the first-install package.

The prepared package is:

```text
/Users/rorosaga/Documents/roros_lab/modpod/dist/themes/piplupos.zip
```

To rebuild it from this checkout:

```sh
cd /Users/rorosaga/Documents/roros_lab/modpod
python3 tools/modpod.py build piplupos
```

Connect the working FAT32/Rockbox iPod. Extract the ZIP **into the root of its storage volume**, merging its `.rockbox` contents with the existing installation. Avoid replacing the entire existing `.rockbox` folder. macOS's `ditto` can perform the merge:

```sh
/usr/bin/ditto -x -k \
  '/Users/rorosaga/Documents/roros_lab/modpod/dist/themes/piplupos.zip' \
  '/Volumes/ACTUAL_IPOD_VOLUME_NAME'
```

Replace the volume-name placeholder with the verified iPod path. This is a manual device-copy command, not a project helper; it has not been run here. The archive contains theme skins/assets/fonts, not firmware.

Safely eject, start Rockbox, then select **Settings → Theme Settings → Browse Theme Files → PiplupOS**. Check album art or the water fallback, Piplup's overlap, bold metadata, battery fill, Shuffle On/Off, pause/resume and menu navigation.

The standard theme dances at fixed timing and puts headphones at the neck immediately on pause. Its WPS and SBS passed the **stable 4.0 skin parser** on this Mac. Native GUI checks used a modified development simulator; physical smoothness, power cost and device behavior remain untested. Early boot branding and Suki's cameo are still pending.

## 5. Put the preserved songs back and index them

For both Apple and Rockbox access, import any recovered audio into Music on the Mac and resync in Apple firmware. Keep the verified backup until songs play in both firmware paths. Do not delete it just because a transfer finishes.

If you only need immediate Rockbox access, copy the backed-up audio into a `/Music` folder on the iPod. Do not also resync the same library through Apple unless you intend to replace that temporary copy, or it will occupy space twice.

For the shared Apple-synced library:

1. Copy `design/piplupos/shared-music.cfg` to the iPod's root, then select it in Rockbox's Files browser to load it. If necessary, set the file view to All. It enables scanning of `/iPod_Control/Music` and `/Music` separately from theme settings.
2. Choose **Settings → General Settings → Database → Initialize Now** once. Wait for indexing and follow any restart prompt.
3. Browse Database by artist, album or track. **Database → Shuffle Songs** shuffles the library; **Settings → Playback Settings → Shuffle** changes the current playlist's shuffle setting. PiplupOS displays that state during playback.
4. After later Apple syncs, let Auto Update finish or choose **Update Now**. Avoid repeated initialization if you want to retain Rockbox's play counts and ratings.

Unprotected M4A/AAC, ALAC and MP3 are supported. DRM-protected subscription downloads are not ordinary playable files. Apple's artwork database is separate: album covers need a supported embedded JPEG or Rockbox cover file, otherwise the theme shows water. Details and primary sources: [shared-music guide](SHARED_MUSIC.md).
