import json, os, hashlib, io
import requests
from PIL import Image
d=json.load(open('articles.json',encoding='utf-8'))
H={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36','Referer':'https://mp.weixin.qq.com/'}
outdir=os.path.join(os.path.dirname(os.path.abspath(__file__)),'imgs')
os.makedirs(outdir,exist_ok=True)
sess=requests.Session()
def fetch(url):
    try:
        r=sess.get(url,headers=H,timeout=30)
        if r.status_code!=200 or len(r.content)<2000: return None
        im=Image.open(io.BytesIO(r.content)); im.load()
        return im
    except Exception as e:
        return None
for rec in d:
    n=rec['n']; 
    seq=0
    for u in rec.get('images',[]):
        seq+=1
        im=fetch(u)
        if im is None: continue
        w,h=im.size
        if w<160 or h<120: continue
        ext='png' if im.mode in ('RGBA','P') else 'jpg'
        im.convert('RGB').save(os.path.join(outdir,f"{n:02d}-{seq:02d}.jpg"),'JPEG',quality=82)
    print(n,'done',flush=True)
