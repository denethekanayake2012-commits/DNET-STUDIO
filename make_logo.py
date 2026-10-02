from PIL import Image, ImageDraw
S=256
im=Image.new("RGBA",(S,S),(5,7,17,255))
d=ImageDraw.Draw(im)
d.rounded_rectangle((0,0,255,255),radius=64,fill=(5,7,17,255))
d.ellipse((16,16,240,240),outline=(79,140,255,255),width=8)
d.ellipse((24,24,232,232),outline=(157,92,255,255),width=4)
m=Image.new("L",(S,S),0)
md=ImageDraw.Draw(m)
md.rectangle((88,64,140,192),fill=255)
md.ellipse((108,64,196,192),fill=255)
md.rectangle((108,91,142,165),fill=0)
md.ellipse((110,91,160,165),fill=0)
g=Image.new("RGBA",(S,S))
gp=g.load()
for y in range(S):
    for x in range(S):
        t=(x+y)/(2*(S-1))
        gp[x,y]=(36+int(121*t),224-int(132*t),230,255)
im.paste(g,(0,0),m)
im.save(r"C:\Users\dnets\Desktop\DNET-Studio\assets\dnet-favicon.png","PNG")
print("PNG_CREATED")