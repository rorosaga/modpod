-- Preserve the v5 art and timeline while making a separate faster-timing draft.
local output='design/piplupos/aseprite/piplup-timing-v6.aseprite'
local exists=io.open(output,'rb')
if exists then exists:close(); error('Timing draft exists; preserve any hand edits.') end
local sprite=app.open('design/piplupos/aseprite/piplup-draft-v5.aseprite')
for frame=1,8 do sprite.frames[frame].duration=0.1 end
for frame=10,11 do sprite.frames[frame].duration=0.2 end
for frame=13,15 do sprite.frames[frame].duration=0.2 end
for frame=16,19 do sprite.frames[frame].duration=0.1 end
sprite.data=sprite.data..' V6 timing: 100ms playing poses, 200ms headset transitions; unchanged v5 pixels and 3-second delay.'
sprite:saveAs(output)
