-- Run from the repository root with Aseprite -b --script this-file.
-- All image manipulation happens inside Aseprite; generated art remains a draft.
local sourcePath = "design/piplupos/concepts/mascot-headbob-v1.png"
local outputPath = "design/piplupos/aseprite/piplup-draft-v1.aseprite"
local existing = io.open(outputPath, "rb")
if existing then
  existing:close()
  error("Draft already exists. Keep hand edits; use a new versioned output path.")
end

local source = Image{ fromFile=sourcePath }
assert(source.width == 2172 and source.height == 724,
       "This script is calibrated for the v1 generated concept, not arbitrary input.")
assert(app.pixelColor.rgbaA(source:getPixel(0, 0)) == 0,
       "The concept must have a genuinely transparent background.")

local sprite = Sprite(64, 64, ColorMode.RGB)
local layer = sprite.layers[1]
layer.name = "Mascot draft — clean pixels and align poses"
sprite.data = "PiplupOS draft from generated art. Left-facing, closed eyes, headphones. Native skin and device testing pending."
local poses = {}
for i = 1, 4 do
  -- Equal-width concept cells; crop the shared transparent top/bottom margins.
  local crop = Image(source, Rectangle((i-1)*543, 96, 543, 576))
  crop:resize(60, 64) -- Aseprite's default nearest-neighbor image resize.
  local image = Image(64, 64, ColorMode.RGB)
  image:drawImage(crop, Point(2, 0))
  poses[i] = image
end

for i = 1, 6 do
  if i > 1 then sprite:newEmptyFrame(i) end
  local image = i <= 4 and poses[i] or poses[1]
  sprite:newCel(layer, i, image, Point(0, 0))
  sprite.frames[i].duration = i <= 4 and 0.2 or 1.0
end
local playing = sprite:newTag(1, 4)
playing.name = "playing-draft"
playing.aniDir = AniDir.FORWARD
local paused = sprite:newTag(5, 5)
paused.name = "paused-draft"
local idle = sprite:newTag(6, 6)
idle.name = "idle-draft"
assert(#sprite.frames == 6 and sprite.width == 64 and sprite.height == 64)
sprite:saveAs(outputPath)
print("Saved 64x64, 6-frame Aseprite draft with playing/paused/idle tags. Pixel cleanup pending.")
