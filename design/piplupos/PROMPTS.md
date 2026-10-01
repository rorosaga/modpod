# PiplupOS · Image-generation record

All concepts used the built-in image generation tool on 2026-09-30 and were saved into this project. Aseprite was used to crop, resize, assemble, and export the editable animation drafts.

## Mascot strip · v1

Input: `references/piplup-palette-reference.png` — supplied Piplup identity/palette reference. Output: `concepts/mascot-headbob-v1.png`. Transparent background requested.

Prompt:

> Use case: stylized-concept. Asset type: single transparent pixel-art animation concept strip for a personal iPod Video theme named PiplupOS. The attached reference image is a SUBJECT IDENTITY AND PALETTE reference, not a target to preserve unchanged. Create a new 4-frame sprite concept strip of this Piplup wearing over-ear headphones, facing toward the LEFT in every frame, BOTH EYES CLOSED in a relaxed listening expression in every frame. Match the reference's muted ice-blue, medium denim-blue, navy outlines, and white face/belly, including its chunky chubby proportions and small flippers; do not introduce warm bright yellow or rainbow colors. Headphones ALWAYS visible in every frame: dark navy headband over the head and dark navy/cool-blue cushioned earcups, closed eyes still readable. Three-quarter LEFT-facing body with beak clearly pointing left. Four consecutive head-bob poses in ONE horizontal row with equal, evenly spaced square cells: 1 neutral-up, 2 head dipping forward/down, 3 deeper gentle nod, 4 coming back up; keep the body shape, face identity, headphone design, palette, size, and foot baseline consistent. Each character is drawn as if designed on a 64x64 logical pixel canvas, enlarged by an integer scale with large crisp square pixels, clean one-pixel navy outline, 12-16-color limited palette, no smooth illustration outlines, no antialiasing, no blur. Entire body and headphones visible, ample clear padding inside each cell, no clipping. Genuine transparent background, no drawn checkerboard, no drop shadows, no text, no logo, no panel, no UI, no musical-note decorations. This is a DESIGN REFERENCE to refine in Aseprite, not a promise of a technically valid sprite sheet. The four silhouettes should be big enough for easy review.

Observed output: 2172 × 724 RGBA. The poses need manual pixel/shape cleanup. The Aseprite draft uses equal-width concept cells and a shared crop; the output is not automatically a clean 64 × 64 sprite sheet.

## Screen concept board · v1

Input roles, in tool order:

1. `references/pool-window-reference.png`: primary window/water aesthetic.
2. `concepts/mascot-headbob-v1.png`: generated mascot identity.
3. `references/windows-95-reference.png`: classic UI vocabulary.
4. `references/windows-xp-reference.png`: secondary blue/sky mood.

Output: `concepts/screens-v1.png`. Opaque background requested.

Prompt:

> Use case: ui-mockup. Asset type: a clean visual concept board for PiplupOS, a personal skin on an iPod Video 5.5 with an actual 320x240 pixel screen and click-wheel navigation. Input image 1 is the PRIMARY AESTHETIC reference: grey beveled Windows 95 window chrome, midnight blue title bar, sunlit cyan swimming-pool water, cute nostalgia. Input image 2 is the PRIMARY MASCOT IDENTITY reference: pixel Piplup with cool blue/white palette, always headphones, facing LEFT, eyes CLOSED; choose one pose from its strip, do not paste the entire strip. Input image 3 gives classic 95 UI proportions; input image 4 gives XP-era sky and saturated blue accent mood, secondary only. Create ONE landscape design board with exactly TWO large, crisp enlarged 4:3 screen concepts side by side (same size, no physical iPod chassis), labeled above in small neutral text 'PiplupOS — visual draft'. Each screen must LOOK AS IF it was made at 320x240 and enlarged 3x with nearest-neighbor pixels: readable simple pixel font, chunky crisp 1-pixel outlines, modest bevels, minimal decoration, no modern rounded app cards or modern flat phone UI, no cursors or touch-only gestures. LEFT screen is a click-wheel-oriented HOME MENU: a classic grey window with deep-blue title bar labeled 'PiplupOS', a narrow header showing 87% battery, a short vertical menu with 'Music', 'Now Playing', 'Files', 'Settings', visible selected row blue highlight; soft watery blue outside the window; small headphone Piplup in the lower right as a companion, separate from and not obscuring the list. RIGHT screen is NOW PLAYING: a compact grey beveled window title bar reading 'Now Playing', calm cropped cyan pool-water backdrop inside part of the window, text 'Weird Fishes', 'Radiohead', and 'In Rainbows' rendered clearly in a simple pixel text area; a clear progress bar, time '2:11 / 5:18', and a small transport status 'Playing'; a relatively small left-facing closed-eye Piplup with headphones in the lower right, as if nodding along. Balance room for track text and art, mascot only around 48-64 native pixels high, no giant mascot swallowing interface. The board's surrounding background is plain warm light grey; underneath in unobtrusive small text 'Concept only · native layout and feature coverage pending'. Do not imply the skin replaces Apple firmware or has implemented movie/notes/search features. No Microsoft logos, no duck (the duck photo is mood only), no glossy photoreal character, no blurry tiny unreadable UI, no giant bevels. Preserve the mascot's chubby proportions and muted blue/white/navy colors, with eyes closed and headphones in BOTH mockups. This is a FIRST AESTHETIC DRAFT for discussion, not final working firmware.

Observed output: a visual board, not exact native-resolution screens. Layout, font metrics, bevel size, contrast, and feature coverage require reconstruction and review before implementation.

## Light-grey screen board · v2

Input: `concepts/screens-v1.png` — edit target. Output: `concepts/screens-v2-light-grey.png`. Built-in edit, opaque background. Only UI grey was requested to change; the mascot palette remains unchanged.

Prompt:

> Use case: precise-object-edit. Asset type: revised PiplupOS UI concept board. Image 1 is the EDIT TARGET. Change only the grey UI window panels, window chrome and menu rows to a substantially LIGHTER cool light grey, approximately #E9EDF1 with near-white #F4F6F8 highlights and grey thin bevel shadows. Maintain readable navy/black text, crisp pixel typography and classic Windows95-style bevels. The surrounding presentation background can be pale grey too. Keep the existing two-screen layout, deep navy title bars, vivid blue selection, cyan swimming pool water, all labels and text, icons, and Piplup mascots exactly as in the target. Do not lighten or recolor Piplup: preserve his small chunky shape and existing muted blue/white/navy palette, facing left, eyes closed, headphones on. Do not change screen structure, remove functions, add graphics, or introduce rounded modern cards. This is a visual draft only, not implemented firmware. The user's lighter-grey request is specifically for the UI, not the character.

Observed output: lighter cool-grey panels with the two-screen composition, water, navy title bars, and character palette retained. Still a concept board, not a native theme.

## Headphones-to-neck poses · v2

Input roles in tool order:

1. `concepts/mascot-headbob-v1.png`: primary liked identity, chunky proportions, palette, and style.
2. `references/piplup-physique-pixel-left.png`: anatomy reference.
3. `references/piplup-physique-front.png`: anatomy reference.

Output: `concepts/mascot-headphones-neck-v2.png`. Built-in generation with transparent background.

Prompt:

> Use case: stylized-concept. Asset type: transparent 4-pose pixel-art headset transition strip for PiplupOS. Input 1 is PRIMARY identity/palette/style reference: our already liked short chunky Piplup with muted ice-blue, denim-blue, white and navy palette and navy headphones. Keep that character's size, cute round huge head, short broad body and small flippers; do not replace it with a tall or slim official illustration. Input 2 is anatomy reference only for beak, collar, two white belly spots, flippers, tail and feet; retain INPUT 1's cool monochromatic blue palette, not reference 2's yellow feet. Input 3 is anatomy silhouette reference only, not rendering style. Create ONE horizontal strip with EXACTLY FOUR evenly spaced, equal-width square transparent cells, full-body Piplup in each, same foot baseline and scale. He faces LEFT in all four poses, beak pointing left, eyes ALWAYS CLOSED. Navy outlines and crisp enlarged square pixels as if 64x64 logical sprites, approximately 12-16 colors, no antialiasing, no blur. Four poses depict ONE pair of headphones being lowered from head to NECK: cell 1 neutral with headphones ON head and flippers at sides; cell 2 both flippers grasp the two earcups and lift headband slightly above crown, headphones still near ears; cell 3 headband moving forward/down below chin with bare crown, flippers guiding earcups toward neck; cell 4 relaxed, flippers down, headphones resting AROUND NECK with two earcups on upper chest, headband curving behind neck, crown completely bare. Keep round body, face/beak, same closed-eye smile, blue collar, two white belly spots and all character colors consistent in all 4 poses. One headset total in each pose; no duplicate headset on head when around neck. This sequence can be reversed to put them back on. Clear generous transparent padding, no overlaps between cells, no clipping of flippers/headphone band/feet, no text, no UI, no musical notes, no labels, no background or checkerboard, no ground shadow. Actual transparent alpha. This is an animation design reference to refine in Aseprite.

Observed output: 2172 × 724 RGBA, four headset poses. Aseprite v2 combines them with v1 playback poses using a shared crop and nearest-neighbor resize. Shape consistency, edge cleanup, and additional transition frames remain manual work. The output depicts the requested neck-rest state; it does not implement music-state triggers.

## Round head and two-lobed collar · playback v3

Inputs: `concepts/mascot-headbob-v1.png` — edit target; `references/piplup-physique-front.png` and `references/piplup-physique-side.png` — anatomy references.

Output: `concepts/mascot-headbob-v3-round-collar.png`. Built-in image edit; transparent background.

Prompt:

> Use case: precise-object-edit. Asset type: corrected four-frame PiplupOS pixel mascot playback strip. Image 1 is the EDIT TARGET: keep its 4 left-facing, eyes-closed, headphone-wearing head-bob poses, short chunky body, size, foot baseline, generous transparent padding, and muted ice-blue/denim/white/navy palette. Images 2 and 3 are Piplup ANATOMY REFERENCES specifically for round head and blue neck collar. Correct these TWO anatomy problems in EVERY frame consistently: (1) Head/face is a simple round ball with a continuous rounded pixel contour from crown around cheeks and chin. Remove the odd outward rear-cheek bulge/point at the right-lower side of his head under the earcup, and any square jaw/muzzle/extra cheek lump. Do not fuse the head with shoulder/flipper/collar. Apart from the small beak pointing LEFT, no protruding face lobes; white face marking fits INSIDE the round head. Headphones are an external accessory, not a cheek. (2) Piplup has a darker-blue TWO-LOBED SCALLOPED COLLAR directly below the chin, as in anatomy references: two small rounded drooping bib/cape lobes across the upper chest, separated by a shallow central notch, with the nearer lobe larger in three-quarter view. Make these clearly visible and separate from his two light-blue arm flippers and from the two white belly spots. Do not turn the collar into a skinny plain neckband, a scarf, spiky feather tufts, or extra wings. Place the two actual flippers LOWER at the sides of the torso, not sticking out from the cheeks. Preserve overall chunky cute chibi physique, relaxed CLOSED eye in every pose, LEFT-pointing beak, blue monochromatic palette (do not import yellow from official references), and same navy earcups/headband. Minimal head nod between frames; keep circle/head diameter and collar shape consistent, do not stretch the face. Clean crisp enlarged logical 64x64 pixel art, no antialiasing, no smoothing, no stray pixels. EXACTLY FOUR equally spaced cells in ONE horizontal row, same scale and centered composition as edit target, full body visible. Transparent alpha background, no checkerboard, no text, no decorative music symbols, no shadows or UI. Correct anatomy without redesigning the liked character.

Observed output: 2172 × 724 RGBA, four playback poses. Collar has two rounded darker-blue lobes; the head contour no longer projects into the raised shoulder. The chunky silhouette and cool palette remain.

## Round head and two-lobed collar · headset v3

Inputs: `concepts/mascot-headphones-neck-v2.png` — edit target; corrected playback v3 — matching character reference; `references/piplup-physique-front.png` — anatomy reference.

Output: `concepts/mascot-headphones-neck-v3-round-collar.png`. Built-in image edit; transparent background.

Prompt:

> Use case: precise-object-edit. Asset type: corrected PiplupOS four-pose headphone-to-neck animation strip. Image 1 is EDIT TARGET: retain its EXACT four headset states and same horizontal equal-width four-cell composition: 1 headphones on head; 2 flippers lifting earcups/headband; 3 headphones lowered below chin; 4 headphones resting around neck, flippers down. Image 2 is PRIMARY corrected character identity/palette/anatomy to MATCH closely: short chunky body, round head without protruding cheek/jaw, and distinct darker denim-blue collar with TWO rounded drooping lobes directly below chin. Image 3 is official ANATOMY reference showing the blue two-lobed collar and round ball-shaped head; do not copy its yellow color or smooth style. Apply ONLY the same anatomy corrections from image 2 to all four target poses. The head outline is one continuous round pixel ball, no rear cheek jutting out under the earcup, no projecting lower jaw, no muzzle/extra cheek tuft. White face marking lies inside the round head. Beak is small and points LEFT; eyes CLOSED in every pose. Add the TWO rounded darker-blue collar lobes under chin above the two white belly dots, separate from the two pale-blue flippers. Collar should resemble Piplup's scalloped bib/cape from official ref, not a skinny neckband, not spiky feathers. Keep head/collar separate: arms connect lower at body sides rather than cheeks. When headphones rest at neck, earcups rest in front of the upper chest and can partly overlap the collar, but the collar's scalloped lower edges remain readable. One headset total, bare crown in poses 3 and 4, no extra headset. Match image2's round white-face contour, blue collar and small chunky proportions across the strip; keep its muted ice-blue/denim/white/navy palette and headphone design. No new yellow, no character redesign, no changed foot/body positions, no eye opening, no right-facing pose. Crisp square pixel art as if 64x64 logical sprites enlarged, no antialiasing, no faint stray pixels or dots. Transparent alpha, no background/checkerboard, no text, no panels, no music-note decorations or shadows. Full body and lifted headphone band visible with generous padding. Preserve all four states while fixing round-head and collar anatomy consistently.

Observed output: 2172 × 724 RGBA, same four headset states with corrected head and collar. Earcups at neck rest partially overlap the two collar lobes. Aseprite v3 rebuilds the 19-frame timeline with the existing timing.

## Corrected mascot in UI · v3

Inputs: `concepts/screens-v2-light-grey.png` — edit target; `concepts/mascot-headbob-v3-round-collar.png` — corrected mascot identity reference.

Output: `concepts/screens-v3-round-collar.png`. Built-in image edit; opaque background.

Prompt:

> Use case: precise-object-edit. Asset type: PiplupOS UI concept board mascot anatomy correction. Image 1 is the EDIT TARGET. Change ONLY the two Piplup mascots, one in each screen, to match the corrected character in image 2, which is a FOUR-POSE CHARACTER REFERENCE STRIP, not four characters to insert. Choose one neutral/listening pose per screen. The corrected Piplup has a round head/face with no protruding lower rear-cheek lump under headphones, a clear darker-blue TWO-LOBED rounded scalloped collar beneath his chin, two white round belly spots, flippers lower at body sides distinct from collar, and the SAME liked small chunky proportions. Face LEFT, eyes CLOSED, headphones ON head in both UI screens. Keep exactly the same mascot size, placement and approximate pose as existing board; preserve muted ice-blue/denim/white/navy palette. No new yellow colors. Preserve EVERYTHING ELSE in image1 unchanged: the light cool-grey panels and bevels, dark navy title bars, blue selection, cyan pool water, all typography/labels/icons/music-note icons, both screen layouts, track text, progress bar/time, surrounding presentation background and captions. Do not introduce new UI rows, change the water, alter the palette, or move the mascot to cover text. Round-headed corrected Piplup sprites should use crisp square enlarged pixels, no smooth drawn outline, no blur. Output remains an opaque two-screen visual concept board; not implemented firmware.

Observed output: The two mascots use the corrected round-head/two-lobed-collar anatomy; light-grey panels, blue title bars, water, typography and layouts are retained. Still a visual concept, not native screen output.

## Front-muzzle correction · headset v4

Built-in image generation/edit mode. Output: `concepts/mascot-headphones-neck-v4-small-beak.png`.

Inputs and observed result: V3 headset strip was the edit target; marked feedback located the front-left white muzzle; left-facing official sprite was anatomy reference. This was an intermediate before Rodrigo supplied the preferred beak example.

Prompt:

> Use case: precise-object-edit. Asset type: PiplupOS pixel-art headphone-transition strip, FRONT-FACE correction. Image 1 is EDIT TARGET. Image 2 is the user's red-marked feedback, a LOCATION GUIDE ONLY: the red circles identify the unwanted white protruding FRONT/LEFT cheek/muzzle around and BELOW the beak. Do NOT copy red marks or screenshot/background. Image 3 is a Piplup anatomy reference for a spherical head with a SMALL compact closed beak attached directly to its round white face; do not copy its palette or open eyes. In EVERY one of the four target poses, REMOVE the protruding WHITE SNOUT/MUZZLE/LOWER-CHEEK bump at the FRONT/LEFT of the face. It currently juts outward to the left underneath the beak like a mammal's muzzle; DELETE that extra volume. Continue the round white face/head contour cleanly behind the beak down toward the chin. There must be NO protruding white upper/lower lip, white ring/donut around the beak, projecting white cheek, or open smiling mouth. Replace the oversized hollow/ring-shaped nose with a MUCH SMALLER CLOSED BEAK: a short solid light-blue wedge pointing LEFT, approximately 3-4 logical pixels long, dark navy outline, upper and lower halves meeting, sitting directly on the circular face. Retain cool blue palette; no yellow requested. The only small protrusion allowed from the circular front head is the beak itself. All four characters still face LEFT with eyes CLOSED. Preserve everything else: short chunky body, dark-blue TWO rounded drooping collar lobes, flippers and feet, white belly dots, same headset and exact 4 headset states (on head / lifted by flippers / lowering below chin / resting around neck). Keep cell1/3/4 round face silhouette consistent, and correct cell2's beak too. Do not merely change the rear/right side of the head: the requested correction is the FRONT LEFT area explicitly circled in red. Do not make the Piplup taller or slimmer or shift the palette. Exactly four equally spaced cells in one horizontal row, same full-body scale and foot baseline. Crisp enlarged square pixel art as if logical64x64, no blur/antialiasing/smooth cartoon outlines, no stray pixels. Transparent alpha background, no checkerboard, no text/UI/notes/shadows/red annotations. The front protruding white muzzle must visibly disappear; this is a targeted correction, not a full redesign.

## Front-muzzle correction · playback v4

Built-in image generation/edit mode. Output: `concepts/mascot-headbob-v4-small-beak.png`.

Inputs and observed result: V3 playback strip was the target; corrected v4 headset and marked feedback guided the change. Intermediate only; not the selected current face.

Prompt:

> Use case: precise-object-edit. Asset type: PiplupOS corrected playback/head-bob pixel sprite strip. Image 1 is EDIT TARGET, four head-bob poses. Image 2 is PRIMARY CORRECTED FACE REFERENCE: choose its neutral pose for face identity and compact solid closed beak, without the protruding white muzzle. Image 3 is the user's MARKED LOCATION GUIDE only, not artwork to copy: red circles show the unwanted white FRONT/LEFT cheek/muzzle under and around the beak. Correct ONLY that front-left face/beak area in ALL four target playback poses to closely match image2. REMOVE the white projecting lower cheek/snout, white lip, white ring around beak and hollow/donut-like big nose. The head/white face must have one continuous ROUND contour behind a very SMALL short CLOSED solid light-blue beak pointing LEFT. Beak approximately 3-4 logical pixels long with navy outline, no open mouth or ring, no extra white volume jutting beneath it. Only the small beak itself protrudes slightly from the circular face. Especially correct the downward-nodding third pose: no white chin/snout projecting left there either; keep the same spherical head rather than stretching into a muzzle. Keep ALL OTHER details as target: dark blue two-lobed collar below chin, flippers at body sides, chunky small proportions, same ice-blue/denim/white/navy palette, eyes CLOSED every frame, left-facing every frame, headset on head every frame, same four head-bob positions, size, foot baseline and overall composition. No yellow colors, no revised body shape or headset design. Exactly four equally spaced cells in one horizontal strip; full body/headphones visible with transparent padding. Crisp enlarged square pixels as if a64x64 logical sprite, no blur/smooth outline/antialiasing/stray dots. Genuine transparent alpha, no checkerboard, text, UI, music symbols, red marks or ground shadows. The front white muzzle bulge must be removed, not merely a rear/right cheek tweak.

## Preferred character cutout · headset v5

Built-in image generation/edit mode. Output: `concepts/mascot-headphones-neck-v5-preferred-face.png`.

Inputs and observed result: The supplied preferred-face screenshot was the edit target. Transparent output is 1959 × 803. Used as the current headset-pose reference; generated cutout edges still need pixel review.

Prompt:

> Use case: background-extraction. Asset type: transparent PiplupOS four-pose headset strip. The supplied image is the EXACT EDIT TARGET and preferred character reference. Remove ONLY the dark grey screenshot background and preserve ALL FOUR pixel-art Piplup poses and their existing art. Keep the full bodies, pixel geometry, ROUND white face contour beneath the beak, the exact small two-part BLUE beak with dark horizontal seam, closed eyes, navy headphones, two rounded denim-blue collar lobes, body/flippers/feet/white belly spots, proportions and all colors. Do NOT redesign, repaint, simplify, shrink the beak, make a nose, add a white muzzle bump beneath it, or recolor anything. Keep all four headset states in a single horizontal row in their existing order: on head, lifting, lowering, neck rest. Preserve the reference's beak and head contour exactly because those are the desired correction. Keep crisp square pixel edges and whole headband/feet visible; no smoothing/antialiasing, no text, no marks, no extra details, no shadow. Output a genuinely TRANSPARENT alpha background, not a dark background or drawn checkerboard. You may add transparent padding around the strip if needed, while retaining equal-width cells and consistent scale/foot baseline. This is cutout extraction of the user's preferred art, not a new character generation.

## Preferred face · playback v5

Built-in image generation/edit mode. Output: `concepts/mascot-headbob-v5-preferred-face.png`.

Inputs and observed result: The transparent preferred v5 headset strip was the character reference, using its neutral first pose. Transparent output is 1958 × 803. Aseprite matches neutral height across both strips and rebuilds the 19-frame demo.

Prompt:

> Use case: stylized-concept. Asset type: PiplupOS FOUR-FRAME gentle head-bob pixel animation strip. Input is the PRIMARY exact preferred CHARACTER/FACE/PALETTE reference. Use its FIRST pose (headphones on head) as the base character for ALL four new playback frames. Match that reference closely: round white face/head contour smoothly continuing below beak, compact blue upper/lower beak with dark horizontal seam, NO jutting white muzzle or lower-cheek/snouted lip beneath the beak, CLOSED eyes, left-facing, dark blue two-rounded-lobe collar beneath chin, short chunky body, pale-blue flippers, two white belly dots, blue/white feet, same muted blue/white/navy palette and same dark navy headphones. Keep the preferred beak SHAPE AND SIZE and dark dividing line; don't shrink it into a button nose or reshape it into a big hollow ring or mammal muzzle. Exactly FOUR evenly spaced equal-size cells in ONE horizontal row, full character visible. All four characters have headphones ON HEAD throughout, NEVER at neck in this strip. Pose1 is preferred neutral pose; pose2 gently nods down by a small amount; pose3 dips slightly further; pose4 returns toward neutral to close the loop. Move head and headphones together while preserving round head diameter/shape, beak anatomy, body size, foot baseline and collar. Keep motion modest and character consistent, not four different body/face designs. All CLOSED eyes, all face LEFT. Crisp enlarged square pixels, as if 64x64 logical pixel sprites, limited existing palette, no smooth or antialiased outlines, no blur, no stray pixels. Transparent alpha background, no checkerboard/dark background, no UI/text/symbols/musical notes/shadows. Generous clear padding so headband and feet stay unclipped. The original base pose is the face reference the user specifically prefers; preserve its round cheek and small blue two-part beak anatomy.

## Preferred mascot in UI · v5

Built-in image generation/edit mode. Output: `concepts/screens-v5-preferred-face.png`.

Inputs and observed result: V3 screen board was the edit target; the v5 preferred headset strip supplied the mascot. Light-grey UI remains; current mascots use the preferred face. Opaque concept board only.

Prompt:

> Use case: precise-object-edit. Asset type: PiplupOS UI draft with user's preferred mascot face. Image1 is EDIT TARGET, keep this two-screen light-grey Windows95/pool-water UI board. Image2 is PRIMARY PREFERRED CHARACTER REFERENCE: choose its first pose (headphones ON head) for the two mascots. Change ONLY the Piplup sprites in both screens to closely match image2's preferred anatomy: continuous ROUND white face contour underneath the beak without any white projecting snout/lower cheek; compact TWO-PART blue beak with dark horizontal dividing seam exactly as reference; closed eyes, left-facing, dark navy headphones ON head, two rounded darker-blue collar lobes beneath chin, small chunky body, existing cool blue/white/navy palette, white belly spots. Do not simplify the beak into a tiny nose or enlarge it into a hollow ring; preserve preferred shape/size and smooth round cheek beneath it. Keep mascot placement and existing UI mascot size and all other screen content unchanged: light-grey chrome, navy title bars, cyan water, selection, typography/labels/icons, progress bar, time/track text, status/captions and the two-screen layout. Headphones on head for both, no entire reference strip inserted, no new characters, no yellow colors. Crisp enlarged square pixel art, no smoothing/blur. Opaque board. Only update the mascots to the preferred face reference; this remains a visual concept, not implemented firmware.
