"""Post-build: los title con "quote": true en reel.json salen en Montserrat ExtraBold (en vez de titleFont)."""
import json, re, sys
p = sys.argv[1]
reel = json.load(open(f'{p}/reel.json'))
starts = {f"{i['start']:.3f}" for i in reel['inserts'] if i['type'] == 'title' and i.get('quote')}
h = open(f'{p}/index.html', encoding='utf-8').read()
n = 0
def fix(m):
    global n
    if m.group(2) in starts:
        n += 1
        return m.group(1) + "font-family:'Montserrat',sans-serif;font-weight:800;line-height:1;letter-spacing:-0.5px;text-shadow:0 4px 22px rgba(0,0,0,.6),0 2px 6px rgba(0,0,0,.35);" + m.group(3)
    return m.group(0)
h = re.sub(r'(<div id="title\d+" class="clip title cal" data-start="([\d.]+)"[^>]*style=")([^"]*")', fix, h)
open(f'{p}/index.html', 'w', encoding='utf-8').write(h)
print(f'quote_font: {n} títulos en Montserrat')
