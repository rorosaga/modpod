-- Run from the repository root with Aseprite -b --script this-file.
-- Timeline is a behavior demonstration, not a running Rockbox state machine.
local outputPath = "design/piplupos/aseprite/piplup-draft-v3.aseprite"
local existing = io.open(outputPath, "rb")
if existing then
  existing:close()
  error("Draft already exists. Preserve hand edits and choose a new version.")
end

local function cleanEdges(image)
  -- Remove faint generated fringe without altering the opaque blue palette.
  local pc = app.pixelColor
  local cleaned = Image(image)
  for y = 0, image.height-1 do
    for x = 0, image.width-1 do
      local color = image:getPixel(x, y)
      local alpha = pc.rgbaA(color)
      if alpha < 128 then
        cleaned:putPixel(x, y, pc.rgba(0, 0, 0, 0))
      else
        cleaned:putPixel(x, y, pc.rgba(pc.rgbaR(color), pc.rgbaG(color), pc.rgbaB(color), 255))
      end
    end
  end
  -- Drop disconnected single-pixel specks; retain connected outline details.
  local result = Image(cleaned)
  for y = 0, cleaned.height-1 do
    for x = 0, cleaned.width-1 do
      if pc.rgbaA(cleaned:getPixel(x, y)) > 0 then
        local connected = false
        for dy = -1, 1 do
          for dx = -1, 1 do
            local nx, ny = x+dx, y+dy
            if (dx ~= 0 or dy ~= 0) and nx >= 0 and nx < cleaned.width
               and ny >= 0 and ny < cleaned.height
               and pc.rgbaA(cleaned:getPixel(nx, ny)) > 0 then
              connected = true
            end
          end
        end
        if not connected then result:putPixel(x, y, pc.rgba(0, 0, 0, 0)) end
      end
    end
  end
  return result
end

local function importPoses(path)
  local source = Image{ fromFile=path }
  assert(source.width == 2172 and source.height == 724,
         "Crop is calibrated for the generated 2172x724 four-cell strips.")
  assert(app.pixelColor.rgbaA(source:getPixel(0, 0)) == 0,
         "Concept must retain transparent alpha.")
  local poses = {}
  for i = 1, 4 do
    -- The shared crop includes the lifted headband, with a common foot baseline.
    local crop = Image(source, Rectangle((i-1)*543, 64, 543, 608))
    crop:resize(57, 64)
    local image = Image(64, 64, ColorMode.RGB)
    image:drawImage(crop, Point(3, 0))
    poses[i] = cleanEdges(image)
  end
  return poses
end

local playing = importPoses("design/piplupos/concepts/mascot-headbob-v3-round-collar.png")
local headset = importPoses("design/piplupos/concepts/mascot-headphones-neck-v3-round-collar.png")
local sprite = Sprite(64, 64, ColorMode.RGB)
local layer = sprite.layers[1]
layer.name = "Piplup — pixel cleanup pending"
sprite.data = "PiplupOS v3 anatomy correction: round head without rear-cheek bulge, two rounded dark-blue collar lobes. Behavior demo. Left-facing, closed eyes, blue palette. Playback bob -> 3s pause/stop delay -> headset to neck -> reverse on resume. Native event binding unverified."

local timeline = {}
for cycle = 1, 2 do
  for pose = 1, 4 do
    timeline[#timeline+1] = {image=playing[pose], duration=0.2}
  end
end
timeline[9] = {image=headset[1], duration=3.0}
timeline[10] = {image=headset[2], duration=0.25}
timeline[11] = {image=headset[3], duration=0.25}
timeline[12] = {image=headset[4], duration=2.0} -- Review hold; real idle holds until resume.
timeline[13] = {image=headset[3], duration=0.25}
timeline[14] = {image=headset[2], duration=0.25}
timeline[15] = {image=headset[1], duration=0.25}
for pose = 1, 4 do
  timeline[15+pose] = {image=playing[pose], duration=0.2}
end

for i, item in ipairs(timeline) do
  if i > 1 then sprite:newEmptyFrame(i) end
  sprite:newCel(layer, i, item.image, Point(0, 0))
  sprite.frames[i].duration = item.duration
end
local tags = {
  {"playing-draft", 1, 8},
  {"stop-delay-draft", 9, 9},
  {"taking-off-draft", 10, 11},
  {"headphones-neck-draft", 12, 12},
  {"putting-on-draft", 13, 15},
  {"resumed-playing-draft", 16, 19}
}
for _, definition in ipairs(tags) do
  local tag = sprite:newTag(definition[2], definition[3])
  tag.name = definition[1]
  tag.aniDir = AniDir.FORWARD
end
assert(#sprite.frames == 19 and sprite.width == 64 and sprite.height == 64)
sprite:saveAs(outputPath)
print("Saved 64x64, 19-frame v3 corrected anatomy demonstration. Pixel cleanup and Rockbox binding pending.")
