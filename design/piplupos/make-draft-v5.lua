-- Run from the repository root with Aseprite -b --script this-file.
-- Timeline is a behavior demonstration, not a running Rockbox state machine.
local outputPath = "design/piplupos/aseprite/piplup-draft-v5.aseprite"
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
  assert((source.width == 1958 or source.width == 1959) and source.height == 803,
         "The v5 source strips use a 1958/1959x803 reference-sized canvas.")
  assert(app.pixelColor.rgbaA(source:getPixel(0, 0)) == 0,
         "Concept must retain transparent alpha.")
  local bounds = {}
  local top, bottom = source.height, -1
  for i = 1, 4 do
    local left = math.floor((i-1)*source.width/4 + 0.5)
    local right = math.floor(i*source.width/4 + 0.5) - 1
    local box = {left=right, right=left, top=source.height, bottom=-1,
                 cellLeft=left, cellWidth=right-left+1}
    for y = 0, source.height-1 do
      for x = left, right do
        if app.pixelColor.rgbaA(source:getPixel(x, y)) >= 192 then
          box.left = math.min(box.left, x)
          box.right = math.max(box.right, x)
          box.top = math.min(box.top, y)
          box.bottom = math.max(box.bottom, y)
        end
      end
    end
    assert(box.bottom >= box.top, "Each source cell must contain a pose.")
    bounds[i] = box
    top = math.min(top, box.top)
    bottom = math.max(bottom, box.bottom)
  end
  -- Map the neutral character to 50 pixels tall for both source strips.
  -- Shared top/bottom keeps the raised headset and foot baseline aligned.
  local scale = 50 / (bounds[1].bottom-bounds[1].top+1)
  local height = math.floor((bottom-top+1)*scale + 0.5)
  assert(height <= 59, "Pose would exceed the padded 64px canvas.")
  local poses = {}
  for i, box in ipairs(bounds) do
    local crop = Image(source, Rectangle(box.cellLeft, top, box.cellWidth, bottom-top+1))
    local width = math.floor(box.cellWidth*scale + 0.5)
    crop:resize(width, height)
    local center = (box.left+box.right)/2 - box.cellLeft
    local px = math.floor(32-center*width/box.cellWidth + 0.5)
    local image = Image(64, 64, ColorMode.RGB)
    image:drawImage(crop, Point(px, 61-height))
    poses[i] = cleanEdges(image)
  end
  print(path .. ": neutral=50px, foot baseline=60, shared crop height=" .. height)
  return poses
end

local playing = importPoses("design/piplupos/concepts/mascot-headbob-v5-preferred-face.png")
local headset = importPoses("design/piplupos/concepts/mascot-headphones-neck-v5-preferred-face.png")
local sprite = Sprite(64, 64, ColorMode.RGB)
local layer = sprite.layers[1]
layer.name = "Piplup — pixel cleanup pending"
sprite.data = "PiplupOS v5 preferred-face correction: round face below compact two-part blue beak, no white front muzzle; two blue collar lobes. Behavior demo. Left-facing, closed eyes, blue palette. Playback bob -> 3s pause/stop delay -> headset to neck -> reverse on resume. Native event binding unverified."

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
local review = Image(256, 64, ColorMode.RGB)
review:drawImage(playing[1], Point(0, 0))
review:drawImage(playing[3], Point(64, 0))
review:drawImage(headset[2], Point(128, 0))
review:drawImage(headset[4], Point(192, 0))
review:resize(1024, 256)
review:saveAs("design/piplupos/previews/piplup-face-review-v5.png")
print("Saved 64x64, 19-frame v5 preferred-face demonstration. Pixel cleanup and Rockbox binding pending.")
