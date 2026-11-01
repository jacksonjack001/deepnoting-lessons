import re, json, os, sys, time, hashlib
import requests
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, '..', '261030.txt')
OUT = BASE
COOKIE = sys.argv[1] if len(sys.argv) > 1 else ''

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}
if COOKIE:
    HEADERS['Cookie'] = COOKIE

raw = open(SRC, encoding='utf-8').read()
cur_date = None
items = []
for ln in raw.splitlines():
    ln = ln.strip()
    m = re.match(r'^(\d{4})年(\d{1,2})月(\d{1,2})日', ln)
    if m:
        cur_date = f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
        continue
    m = re.match(r'^\[链接\]\s*(.*?)\s*(https?://\S+)$', ln)
    if m:
        items.append({'title': m.group(1), 'url': m.group(2), 'fwd_date': cur_date})

sess = requests.Session()

def canon(url):
    import urllib.parse as up
    p = up.urlparse(url)
    q = up.parse_qs(p.query)
    # canonical key = biz + mid + idx + sn if present else path
    if 'mid' in q and 'idx' in q:
        return f"{q.get('__biz',[''])[0]}|{q['mid'][0]}|{q['idx'][0]}|{q.get('sn',[''])[0]}"
    return p.path + '?' + p.query

results = []
for i, it in enumerate(items, 1):
    rec = dict(it)
    rec['n'] = i
    try:
        r = sess.get(it['url'], headers=HEADERS, timeout=30)
        r.encoding = 'utf-8'
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        # title
        t = soup.find('h1', class_='rich_media_title') or soup.find('h1', id='activity-name')
        rec['wx_title'] = t.get_text(strip=True) if t else ''
        # publisher
        pub = soup.find('a', id='js_name') or soup.find('span', class_='rich_media_meta_text') 
        pubn = soup.find('a', class_='rich_media_meta rich_media_meta_link rich_media_meta_nickname') or soup.find('strong', class_='profile_nickname')
        rec['publisher'] = pubn.get_text(strip=True) if pubn else ''
        # date
        dt = soup.find('em', id='publish_time')
        rec['pub_date'] = dt.get_text(strip=True) if dt else ''
        # body
        body = soup.find('div', id='js_content')
        rec['body_text'] = body.get_text('\n', strip=True) if body else ''
        imgs = []
        if body:
            for im in body.find_all('img'):
                src = im.get('data-src') or im.get('src')
                if src and src.startswith('http'):
                    imgs.append(src)
        rec['images'] = imgs
        rec['status'] = r.status_code
        rec['ok'] = bool(rec['body_text'])
    except Exception as e:
        rec['error'] = str(e)[:200]
        rec['ok'] = False
    results.append(rec)
    print(f"[{i}] {rec.get('status','ERR')} imgs={len(rec.get('images',[]))} bodylen={len(rec.get('body_text',''))} {rec['title'][:30]}", flush=True)
    time.sleep(0.4)

json.dump(results, open(os.path.join(OUT, 'articles.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("saved", len(results))
