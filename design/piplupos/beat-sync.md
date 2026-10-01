# Beat-synchronized Piplup · proposed extension

Status: design only. The current skins play a fixed 100 ms pose sequence; they do not read song BPM or detect beats.

The inspected Rockbox source at `e45936397ee3677c910c9a0c6473184e9755040c` exposes timed skin sublines and playback position, but no built-in BPM/beat-phase skin tag. Matching the tempo alone would adjust dance speed; landing the head bob on the music also needs the first-beat offset or a beat grid. A custom firmware extension is the proposed route.

Proposed implementation:

1. Analyze songs offline on the Mac, with an option to correct uncertain estimates. Store tempo and beat offset/grid in sidecar data keyed to the song; leave audio and Apple music files untouched. Account for Apple sync renaming files.
2. Load timing for the current song in Rockbox and expose a beat-phase/frame selector to the skin. Derive phase from elapsed audio position, including playback-speed changes, so seeks and resume do not restart an unrelated animation clock.
3. Use one head-bob cycle per beat or every two beats for faster songs. Freeze or transition to the existing headphone rest state while paused. Keep fixed timing when timing data is missing.
4. Verify synthetic pulse tracks at two tempos, seek/pause/resume, track changes, variable-tempo grids and missing timing before trying the physical iPod. Measure rendering and battery cost on hardware separately.

No analyzer, sidecar loader or firmware beat tag has been implemented. Tempo estimation can be wrong, and live beat detection on the iPod is not assumed feasible within the current performance budget.

References: [official skin tags](https://github.com/Rockbox/rockbox/blob/e45936397ee3677c910c9a0c6473184e9755040c/manual/appendix/wps_tags.tex), [skin tag table](https://github.com/Rockbox/rockbox/blob/e45936397ee3677c910c9a0c6473184e9755040c/lib/skin_parser/tag_table.c).
