# Games on the iPod Video

Open **Plugins → Games**. Individual games have their own controls and may use a separate screen layout; the skin does not replace their gameplay interface. **Brickmania** is the ball-and-paddle brick-breaking game Rodrigo asked about.

## Doom: Missing Base WAD

This message means Doom cannot find a recognised game-data WAD. Rockbox includes the executable, while the data belongs in the hidden `/.rockbox/doom/` folder:

- `rockdoom.wad`: the Rockbox support data.
- A recognised game WAD, such as `doom1.wad` (shareware), `doom2.wad` (owned Doom II), or `doomf.wad` (free Freedoom content).

The [official Rockbox game-data ZIP](https://download.rockbox.org/useful/rockdoom.zip) downloaded on 2026-10-02 contains `rockdoom.wad`, `freedoom1.wad` and `freedoom2.wad`. All three were already on Rodrigo's device, but stock 4.0's plugin recognises Freedoom under the exact filename **doomf.wad**. The update copied the ZIP's `freedoom2.wad` under that name and verified its SHA256, preserving the existing files. It provides Freedoom's free Doom-compatible levels and artwork; it is a different game-data set from the commercial Doom campaign.

With the iPod mounted, merge the support and selected game WAD into `/.rockbox/doom/`. Safely eject, launch **Plugins → Games → doom**, choose **Game → Freedoom**, then **Play Game**. A bootloader or firmware reinstall is unnecessary.

On the ARM64 Mac simulator these files remove “Missing Base WAD” and open the game menu. Starting gameplay crashed the simulator with a bus error. This establishes data detection only; successful gameplay on the physical 32-bit iPod remains unverified.

Sources: [Rockbox Doom manual](https://github.com/Rockbox/rockbox/blob/master/manual/plugins/doom.tex), [stable 4.0 WAD names and error check](https://github.com/Rockbox/rockbox/blob/v4.0-final/apps/plugins/doom/rockdoom.c), [Freedoom project](https://freedoom.github.io/).
