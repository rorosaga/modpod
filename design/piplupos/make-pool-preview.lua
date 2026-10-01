-- Animation illustration over a native renderer capture with static text.
-- This is an asset preview, not a recording of simulator playback.
local capture=app.params['capture']
assert(capture,'Pass --script-param capture=<native PNG>')
local native=app.open(capture)
assert(native.width==320 and native.height==240)
local base=native.layers[1]:cel(1).image
local desktop=app.open('design/piplupos/aseprite/native-desktop.aseprite')
local noCover=app.params['no-cover']=='1'
local mascot=noCover and app.open('design/piplupos/aseprite/piplup-timing-v6.aseprite') or nil
local underlay
if noCover then
  underlay=Image{fromFile='themes/piplupos/assets/mascot-underlay.bmp'}
  local pc=app.pixelColor
  for y=0,63 do for x=0,63 do
    local pixel=underlay:getPixel(x,y)
    if pc.rgbaR(pixel)==255 and pc.rgbaG(pixel)==0 and pc.rgbaB(pixel)==255 then
      underlay:putPixel(x,y,pc.rgba(0,0,0,0))
    end
  end end
end
local preview=Sprite(320,240,ColorMode.RGB)
for phase=1,#desktop.frames do
  if phase>1 then preview:newEmptyFrame() end
  local im=Image(base)
  local pool=desktop.layers[1]:cel(phase).image
  for _,strip in ipairs({{0,0,320,9},{0,231,320,9},{0,9,9,222},{311,9,9,222}}) do
    im:drawImage(Image(pool,Rectangle(table.unpack(strip))),Point(strip[1],strip[2]))
  end
  if noCover then
    im:drawImage(underlay,Point(164,49))
    im:drawImage(Image(pool,Rectangle(0,0,103,84)),Point(196,80))
    local cel=mascot.layers[1]:cel((phase-1)%4+1)
    im:drawImage(cel.image,Point(164+cel.position.x,49+cel.position.y))
  end
  preview:newCel(preview.layers[1],phase,im,Point(0,0))
  preview.frames[phase].duration=desktop.frames[phase].duration
end
preview:resize(640,480)
preview:saveAs('design/piplupos/previews/'..(noCover and 'piplupos-motion-preview.gif' or 'pool-border-preview.gif'))
