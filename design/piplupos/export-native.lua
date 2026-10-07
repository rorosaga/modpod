-- Run from modpod with Aseprite --batch --script this file.
-- Original mascot Aseprite remains editable and is never overwritten.
local pc = app.pixelColor
local function color(hex)
  return pc.rgba(tonumber(hex:sub(1,2),16), tonumber(hex:sub(3,4),16), tonumber(hex:sub(5,6),16),255)
end
local c = {bg=color('E9EDF1'), hi=color('F4F6F8'), shadow=color('A3ADBA'),
           line=color('10162F'), navy=color('08086A'), white=color('FFFFFF')}
local waterFrames, frameSeconds = 12, 0.1
local function rect(im,x,y,w,h,col)
  for py=y,y+h-1 do for px=x,x+w-1 do im:putPixel(px,py,col) end end
end
local function bevel(im,x,y,w,h)
  rect(im,x,y,w,h,c.line)
  rect(im,x+1,y+1,w-2,h-2,c.shadow)
  rect(im,x+1,y+1,w-3,1,c.hi)
  rect(im,x+1,y+1,1,h-3,c.hi)
  rect(im,x+2,y+2,w-4,h-4,c.bg)
end
local function saveSource(im,name)
  local sprite=Sprite(im.width,im.height,ColorMode.RGB)
  sprite.layers[1].name='Native PiplupOS chrome'
  sprite:newCel(sprite.layers[1],1,im,Point(0,0))
  sprite:saveAs('design/piplupos/aseprite/native-'..name..'.aseprite')
  im:saveAs('themes/piplupos/assets/'..name..'.bmp')
end
-- One continuous water field surrounds the inset window. Export only the
-- exposed strips so animation never redraws the controls or a full-screen BMP.
local function waterPixel(x,y,phase)
  -- A full angular cycle makes the last-to-first step continuous.
  local angle=2*math.pi*phase/waterFrames
  local wave=math.sin(x*0.15+y*0.07+angle)+math.sin(x*0.08-y*0.19-angle)
  return color(wave>1.5 and '8CE6FA' or wave>0.8 and '4DD0F1' or wave>0 and '20BCE8' or '109FDB')
end
local desktop=Sprite(320,240,ColorMode.RGB)
desktop.layers[1].name='Animated pool desktop'
for phase=0,waterFrames-1 do
  if phase>0 then desktop:newEmptyFrame() end
  local im=Image(320,240,ColorMode.RGB)
  for y=0,239 do for x=0,319 do im:putPixel(x,y,waterPixel(x,y,phase)) end end
  desktop:newCel(desktop.layers[1],phase+1,im,Point(0,0))
  desktop.frames[phase+1].duration=frameSeconds
end
desktop:saveAs('design/piplupos/aseprite/native-desktop.aseprite')
for _,strip in ipairs({{'top',0,0,320,9},{'bottom',0,231,320,9},
                      {'left',0,9,9,222},{'right',311,9,9,222}}) do
  local sheet=Image(strip[4],strip[5]*waterFrames,ColorMode.RGB)
  for phase=0,waterFrames-1 do
    local im=desktop.layers[1]:cel(phase+1).image
    sheet:drawImage(Image(im,Rectangle(strip[2],strip[3],strip[4],strip[5])),Point(0,phase*strip[5]))
  end
  sheet:saveAs('themes/piplupos/assets/pool-'..strip[1]..'.bmp')
end
local playerBackdrop
for _,name in ipairs({'menu','player'}) do
  local im=Image(desktop.layers[1]:cel(1).image)
  bevel(im,9,9,302,222)
  rect(im,12,12,296,19,c.navy)
  bevel(im,291,14,14,14)
  -- Classic raised close button; Menu/Back is the physical iPod action.
  for offset=0,5 do
    im:putPixel(295+offset,18+offset,c.line)
    im:putPixel(300-offset,18+offset,c.line)
  end
  -- Battery outline remains in the backdrop while Rockbox redraws its fill.
  rect(im,230,16,24,10,c.white)
  rect(im,231,17,22,8,c.navy)
  rect(im,254,19,2,4,c.white)
  rect(im,14,208,292,1,c.shadow)
  rect(im,14,209,292,1,c.hi)
  if name=='player' then
    bevel(im,193,63,109,104)
    rect(im,19,171,282,13,c.shadow)
    rect(im,20,172,280,11,c.white)
  else
    rect(im,18,57,284,1,c.shadow)
    rect(im,18,58,284,1,c.hi)
  end
  saveSource(im,name)
  if name=='player' then playerBackdrop=im end
end

-- Legacy underlay export; the native WPS now restores its cached backdrop.
-- Keep the enlarged artwork cutout consistent for older asset previews.
local underlay=Image(playerBackdrop,Rectangle(164,49,64,64))
for y=17,63 do for x=32,63 do underlay:putPixel(x,y,color('FF00FF')) end end
underlay:saveAs('themes/piplupos/assets/mascot-underlay.bmp')

local mascot=app.open('design/piplupos/aseprite/piplup-timing-v6.aseprite')
assert(mascot.width==64 and mascot.height==64 and #mascot.frames==19)
local sheet=Image(64,64*19,ColorMode.RGB)
rect(sheet,0,0,sheet.width,sheet.height,color('FF00FF')) -- Rockbox BMP color key
for frame=1,19 do
  local cel=mascot.layers[1]:cel(frame)
  sheet:drawImage(cel.image,Point(cel.position.x,(frame-1)*64+cel.position.y))
end
sheet:saveAs('themes/piplupos/assets/piplup.bmp')

local water=Image(103,98*waterFrames,ColorMode.RGB)
for frame=0,waterFrames-1 do
  for y=0,97 do for x=0,102 do
    water:putPixel(x,y+frame*98,waterPixel(x,y,frame))
  end end
end
water:saveAs('themes/piplupos/assets/water.bmp')
-- Composite the water and mascot into opaque frames. Rockbox clears each
-- image viewport's text row against its backdrop before redrawing; separate
-- transparent layers otherwise leave a grey stripe across the water.
local function poolFrame(frame,phase)
  local im=Image(water,Rectangle(0,phase*98,103,98))
  local cel=mascot.layers[1]:cel(frame)
  im:drawImage(cel.image,Point(14+cel.position.x,14+cel.position.y))
  return im
end
local pool=Image(103,98*19,ColorMode.RGB)
for frame=1,19 do pool:drawImage(poolFrame(frame,(frame-1)%waterFrames),Point(0,(frame-1)*98)) end
pool:saveAs('themes/piplupos/assets/pool-mascot.bmp')
for _,state in ipairs({{'neck',12},{'hold',9}}) do
  local frames=Image(103,98*waterFrames,ColorMode.RGB)
  for phase=0,waterFrames-1 do frames:drawImage(poolFrame(state[2],phase),Point(0,phase*98)) end
  frames:saveAs('themes/piplupos/assets/pool-'..state[1]..'.bmp')
end
local menuFrames=Image(64,64*4,ColorMode.RGB)
rect(menuFrames,0,0,64,64*4,c.bg)
for frame=1,4 do
  local cel=mascot.layers[1]:cel(frame)
  menuFrames:drawImage(cel.image,Point(cel.position.x,(frame-1)*64+cel.position.y))
end
menuFrames:saveAs('themes/piplupos/assets/menu-mascot.bmp')
local menuNeck=Image(64,64,ColorMode.RGB)
rect(menuNeck,0,0,64,64,c.bg)
local neckCel=mascot.layers[1]:cel(12)
menuNeck:drawImage(neckCel.image,neckCel.position)
menuNeck:saveAs('themes/piplupos/assets/menu-neck.bmp')
print('Exported native BMP backdrops, 19 mascot frames and '..waterFrames..' seamless water frames from Aseprite.')
