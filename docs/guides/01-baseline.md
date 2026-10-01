<!-- Generated from handbook/content.json by tools/modpod.py build. -->
# Keep a working baseline

The original iPod already plays a song. Record that result and prepare for the hardware session.

## Before starting

Use the iPod in Apple firmware before changing hardware. A known working baseline makes later problems easier to isolate.

## 1. Record what works

Playback was confirmed on 30 September 2026. Before opening it, also check the click wheel, headphone output, charging, and USB connection. Add your findings to docs/BUILD_LOG.md.

## 2. Back up anything you want to keep

Keep the source music on the Mac and copy any unique iPod content to a separate backup. The storage restore and FAT32 conversion later will erase the iPod.

## 3. Check your parts

Lay out the Quad, card, battery, and toolkit. Photograph the card label and battery. Compare the received battery with the listing dimensions, and measure the back-shell depth.

## 4. Prepare the workspace

Use a clean, well-lit surface, a parts tray, and the illustrated opening guide. Safely eject the iPod, unplug it, and turn it off before opening.

## Checklist

- [x] Apple-firmware playback confirmed
- [ ] Music and any unique files backed up
- [ ] Controls, charging, audio, and USB baseline recorded
- [ ] Card SKU, battery dimensions, and case depth recorded

## Keep in mind

The baseline was Mac formatted (HFS+). Do not assume it is ready for Rockbox just because it works in Finder.

## Full references

- [iFixit · iPod 5th Generation (Video) battery replacement](https://www.ifixit.com/Guide/iPod+5th+Generation+(Video)+Battery+Replacement/603)
- [iFlash Quad · Product and illustrated installation](https://www.iflash.xyz/store/iflash-quad/)
- [iFlash · Third-party extended battery guide](https://www.iflash.xyz/3rd-party-extended-battery-guide/)
