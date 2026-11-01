import os, sys, glob
from PIL import Image, ImageDraw
def sheet(n, cols=5, tw=320):
    files=sorted(glob.glob(f'imgs/{n:02d}-*.jpg'))
    if not files: 
        print('none',n); return
    ims=[]
    for f in files:
        try:
            im=Image.open(f).convert('RGB'); 
            r=tw/im.width; im=im.resize((tw,max(1,int(im.height*r))))
            if im.height>300: im=im.crop((0,0,tw,300))
            ims.append((os.path.basename(f),im))
        except: pass
    rows=(len(ims)+cols-1)//cols
    H=sum(max(i.height for _,i in ims[r*cols:(r+1)*cols])+18 for r in range(rows))
    sheet=Image.new('RGB',(cols*tw, H),'white'); dr=ImageDraw.Draw(sheet)
    y=0
    for r in range(rows):
        row=ims[r*cols:(r+1)*cols]
        x=0; rh=max(i.height for _,i in row)+18
        for name,im in row:
            sheet.paste(im,(x,y+16)); dr.text((x+2,y+3),name,fill='red')
            x+=tw
        y+=rh
    os.makedirs('sheets',exist_ok=True)
    sheet.save(f'sheets/{n:02d}.jpg','JPEG',quality=80)
    print('sheet',n,len(ims))
for a in sys.argv[1:]:
    sheet(int(a))
