# Modpod

A build notebook and theme workshop for Rodrigo’s iPod Video 5.5 generation.

**Custom design direction: [PiplupOS](design/piplupos/README.md).** A Windows 95/XP-era skin with grey beveled windows, deep-blue title bars, pool-water blues, and a left-facing, closed-eye Piplup wearing headphones. Visual concepts and an Aseprite animation draft live in `design/piplupos/`; Paper and Midnight below are foundation examples, not the selected final theme. [Feature preservation](docs/FEATURE_PRESERVATION.md) uses the dual-boot route approved by Rodrigo: Rockbox/PiplupOS plus the original Apple firmware.

**Current stage:** Rodrigo installed the Quad and replacement battery and confirmed the new 128 GB storage on 30 September. Native Apple Silicon Rockbox Utility and the simulator are installed on his Mac. PiplupOS menus, playback and animation have native simulator checks; physical installation is blocked by the current HFS+ volume. Keep source songs on the Mac for a later FAT32 restore/resync. See [shared music](docs/SHARED_MUSIC.md) and [Mac setup](docs/SIMULATOR.md). Screen pressure and post-mod playback/charging/USB checks remain pending. Development uses a dev branch and pull requests to `main`; simulator binaries, virtual music and generated packages are excluded from Git.

## Open the handbook

```sh
python3 tools/modpod.py serve
```

Open **http://127.0.0.1:8765**. The handbook includes ordered guides, checklists that remember your progress in that browser, purchased parts with credited product photos, a tutorial watchlist, PiplupOS variants and two starter themes. Photos and external tutorials need internet access; the guides and theme mockups work offline.

Checklist changes stay in browser storage. Export them from the Build page to keep a backup. The repository build log is the durable record of what was actually tested. Clearing browser storage, opening a different browser, or changing the address can reset checklist state.

## Make a theme

```sh
python3 tools/modpod.py new my-theme --from piplupos
```

Edit `themes/my-theme/theme.json`, then:

```sh
python3 tools/modpod.py build my-theme
python3 tools/modpod.py serve
```

The palette editor in the handbook can also download an edited `theme.json`. Replace the manifest in its matching theme folder and build again. Packages appear in `dist/themes/` and contain native configuration, WPS/SBS skins, theme bitmaps and bundled fonts with their notices. The `new` command copies native overrides, assets and fonts as well as the manifest. PiplupOS's bitmap palette is edited/exported in Aseprite; changing text tokens alone does not recolor its artwork. See [the workshop](docs/THEME_WORKFLOW.md).

**These are prototypes, not device-tested themes.** The browser shows a generic layout illustration. PiplupOS separately passed native parser and GUI checks recorded in [the build log](docs/BUILD_LOG.md). The standard version animates playback/water and changes immediately on pause. The experimental delayed-headphone version needs custom firmware; stock ipodvideo lacks its timer variables. Paper and Midnight have structural checks only.

## Where things live

| Directory | Purpose |
| --- | --- |
| `docs/` | Start here, staged guides, build log, theme workflow, recovery |
| `hardware/` | Exact purchases, device profile, future build photos |
| `references/` | Primary sources and clearly labeled video references |
| `themes/` | PiplupOS native skins/assets and Paper/Midnight starter examples |
| `templates/ipodvideo/` | Native Rockbox configuration and skin templates |
| `tools/` | Create themes, validate, build, and serve locally |
| `handbook/` | Guide content and local interface source |
| `tests/` | Path safety, overwrite protection, and archive checks |
| `dist/` | Generated packages, excluded from Git |

## Build order

1. Record the working Apple-firmware baseline and back up anything worth keeping.
2. Confirm exact battery clearance, card model, and parts before opening the iPod.
3. Install the Quad and battery using the linked illustrated guides; test before snapping the case closed.
4. Restore Apple firmware and verify storage, controls, charging, and playback.
5. Resolve FAT32 formatting, then install Rockbox using the current official instructions.
6. Test a starter theme, then iterate on your own designs.

The connected iPod was still **HFS+ / Mac formatted** on 1 October. Rockbox requires a **FAT32 / Windows-initialized iPod**. Conversion may erase its songs and require restoring/resyncing; the guide leaves those actions for a later installation session, once backups and the device are confirmed. Apple-synced songs can then be indexed by Rockbox without a second copy.

## Check the foundation

```sh
python3 tools/modpod.py validate
python3 -m unittest discover -s tests -v
```

No third-party Python packages are needed. No command in this project writes to an iPod.

Sources were checked on 30 September 2026. Video titles/descriptions were checked; the videos have not been watched or timestamped. The Amazon purchase links are **Amazon Spain**. Product specifications are advertised values, not measurements. No license has been selected yet; linked product images and third-party tutorials remain their owners’ content.
