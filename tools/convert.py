"""Builds the live static site for Netlify from the design generator.
Usage: python3 tools/convert.py   (run from repo root; writes ./site)
"""
import json, os, re, runpy, shutil, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'site')
SITE_URL = 'https://beaurify-demo.netlify.app'   # change to the final domain at launch

G = runpy.run_path(os.path.join(HERE, 'build.py'))
FILES, SERVICES, AREAS, FAQ_GROUPS, ZONES = G['FILES'], G['SERVICES'], G['AREAS'], G['FAQ_GROUPS'], G['ZONES']
POSTS = G.get('POSTS', [])

def url_for(fname):
    stem = fname[:-len('.dc.html')]
    return '/' if stem == 'Main' else f'/{stem}/'

def unesc(s):
    return H.unescape(s)

BUSINESS = {
    "@context": "https://schema.org",
    "@type": "HealthAndBeautyBusiness",
    "@id": SITE_URL + "/#business",
    "name": "Beautified Studios",
    "url": SITE_URL + "/",
    "telephone": "+1-726-242-2952",
    "email": "beautifiedstudios@gmail.com",
    "priceRange": "$150 - $1,954",
    "address": {"@type": "PostalAddress", "streetAddress": "1603 Babcock Rd, Suite 230", "addressLocality": "San Antonio", "addressRegion": "TX", "postalCode": "78229", "addressCountry": "US"},
    "areaServed": ["San Antonio, TX"] + [a['name'] for a in AREAS],
    "founder": {"@type": "Person", "name": "Brandy Gonzalez", "jobTitle": "Master Injector"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Tuesday", "opens": "09:00", "closes": "18:30"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Wednesday", "Thursday", "Friday"], "opens": "09:30", "closes": "18:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "13:30", "closes": "17:00"},
    ],
    "sameAs": ["https://www.instagram.com/beautified.studios/", "https://www.instagram.com/da.injector/"],
}

def faq_schema(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": unesc(q), "acceptedAnswer": {"@type": "Answer", "text": unesc(a)}} for q, a in pairs if '[' not in a]}

def schemas_for(fname):
    out = [BUSINESS]
    stem = fname[:-len('.dc.html')]
    svc = next((s for s in SERVICES if s['slug'] == stem), None)
    if svc:
        srv = {"@context": "https://schema.org", "@type": "Service", "name": unesc(svc['short']), "serviceType": unesc(svc['short']),
               "provider": {"@id": SITE_URL + "/#business"}, "areaServed": "San Antonio, TX", "description": unesc(svc['meta'])}
        m = re.match(r'^(?:From )?\$([\d,]+)$', svc['price'])
        if m:
            srv["offers"] = {"@type": "Offer", "price": m.group(1).replace(',', ''), "priceCurrency": "USD"}
        out.append(srv)
        out.append(faq_schema(svc['faqs']))
    if stem == 'faq':
        out.append(faq_schema([p for _, items in FAQ_GROUPS for p in items]))
    return out

FACEMAP_JS = '''<script>
(function(){
var Z=%s, cur='lips';
var pins=document.getElementById('fm-pins'), list=document.getElementById('fm-list');
function draw(){
  pins.innerHTML=''; list.innerHTML='';
  Z.forEach(function(z){
    var on=z.id===cur;
    var b=document.createElement('button'); b.type='button'; b.setAttribute('aria-label',z.title); b.textContent=z.num;
    b.style.cssText='position:absolute;left:'+z.x+';top:'+z.y+';transform:translate(-50%%,-50%%);width:34px;height:34px;border-radius:999px;font-family:Jost,sans-serif;font-size:13px;font-weight:500;cursor:pointer;'+(on?'background:#4A1F28;color:#F7F0EC;border:2px solid #F7F0EC;box-shadow:0 0 0 6px rgba(74,31,40,.18);':'background:#F7F0EC;color:#4A1F28;border:2px solid #4A1F28;');
    b.onclick=function(){cur=z.id;draw();}; pins.appendChild(b);
    var r=document.createElement('button'); r.type='button';
    r.style.cssText='display:flex;gap:16px;align-items:baseline;width:100%%;padding:16px 0;background:transparent;border:0;border-top:1px solid #DCC6C1;font-family:inherit;text-align:left;cursor:pointer;color:'+(on?'#4A1F28':'#463A3C');
    r.innerHTML='<span style="font-size:13px;width:24px">'+z.num+'</span><span style="font-family:\\'DM Serif Display\\',Georgia,serif;font-size:24px;'+(on?'font-style:italic':'')+'">'+z.title+'</span>';
    r.onclick=function(){cur=z.id;draw();}; list.appendChild(r);
  });
  var c=Z.filter(function(z){return z.id===cur;})[0];
  document.getElementById('fm-title').textContent=c.title; document.getElementById('fm-tx').textContent=c.tx;
  document.getElementById('fm-price').textContent=c.price; document.getElementById('fm-copy').textContent=c.copy;
  document.getElementById('fm-href').setAttribute('href',c.href);
}
draw();
})();
</script>'''

def convert(fname, src):
    # helmet -> head
    m = re.search(r'<helmet>(.*?)</helmet>', src, re.S)
    helmet = m.group(1).strip() if m else ''
    src = src.replace(m.group(0), '') if m else src
    src = re.sub(r'<script type="text/x-dc"[^>]*>.*?</script>', '', src, flags=re.S)
    src = src.replace('<x-dc>', '').replace('</x-dc>', '')
    # scheduler embeds
    uses_sched = 'dc-import name="Scheduler"' in src
    src = re.sub(r'<dc-import name="Scheduler"(?: preset="(\w+)")?[^>]*></dc-import>',
                 lambda mm: f'<div class="bs-scheduler" data-preset="{mm.group(1) or ""}"><noscript><a href="https://beautifedstudios.glossgenius.com/services">Book on GlossGenius</a></noscript></div>', src)
    # face map
    if fname == 'Main.dc.html':
        src = re.sub(r'<sc-for list="\{\{zones\}\}" as="z"[^>]*>\s*<button[^>]*style="\{\{z.pinStyle\}\}">.*?</sc-for>', '<div id="fm-pins"></div>', src, count=1, flags=re.S)
        src = re.sub(r'<sc-for list="\{\{zones\}\}" as="z"[^>]*>.*?</sc-for>', '<div id="fm-list"></div>', src, count=1, flags=re.S)
        for k, i in [('cur.title', 'fm-title'), ('cur.tx', 'fm-tx'), ('cur.price', 'fm-price'), ('cur.copy', 'fm-copy')]:
            src = re.sub(r'(<p )(style="[^"]*">)\{\{' + re.escape(k) + r'\}\}</p>', r'\1id="' + i + r'" \2</p>', src)
        src = src.replace('<a href="{{cur.href}}"', '<a id="fm-href" href="lip-filler-san-antonio.dc.html"')
        zones = [{k: H.unescape(v) for k, v in z.items()} for z in ZONES]
        for z in zones:
            z['href'] = url_for(z['href'])
        src = src.replace('</body>', (FACEMAP_JS % json.dumps(zones)) + '\n</body>')
    assert '{{' not in src, (fname, src[src.index('{{') - 80: src.index('{{') + 80])
    # links
    stem = fname[:-len('.dc.html')]
    sv = next((x for x in SERVICES if x['slug'] == stem), None)
    src = src.replace('href="#book"', 'href="book.dc.html' + (f'?service={sv["id"]}' if sv else '') + '"')
    src = re.sub(r'href="([A-Za-z0-9_\-]+\.dc\.html)(\?[\w=&]+)?(#[\w\-]+)?"', lambda mm: f'href="{url_for(mm.group(1))}{mm.group(2) or ""}{mm.group(3) or ""}"', src)
    # head extras
    page_url = SITE_URL + url_for(fname)
    title = re.search(r'<title>(.*?)</title>', src, re.S).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', src, re.S).group(1)
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in schemas_for(fname))
    robots = '<meta name="robots" content="noindex">\n' if fname == 'photo-checklist.dc.html' else ''
    extra = (f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
             f'<link rel="canonical" href="{page_url}">\n{robots}'
             f'<meta property="og:type" content="website">\n<meta property="og:title" content="{title}">\n'
             f'<meta property="og:description" content="{desc}">\n<meta property="og:url" content="{page_url}">\n'
             f'<meta property="og:site_name" content="Beautified Studios">\n<meta property="og:image" content="{SITE_URL}/assets/og-image.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="Beautified Studios, beauty studio and injector in San Antonio">\n'
             f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="{title}">\n<meta name="twitter:description" content="{desc}">\n<meta name="twitter:image" content="{SITE_URL}/assets/og-image.png">\n'
             f'<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">\n'
             f'{helmet}\n{ld}')
    src = src.replace('<script src="./support.js"></script>', extra)
    if uses_sched:
        src = src.replace('</body>', '<script src="/assets/scheduler.js" defer></script>\n</body>')
    if fname in ('Main.dc.html', 'book.dc.html'):
        src = src.replace('<body>', '''<body>
<form name="booking" data-netlify="true" netlify-honeypot="bot-field" hidden><input name="treatment"><input name="date"><input name="time"><input name="name"><input name="phone"><input name="email"><input name="notes"><input name="page"><input name="bot-field"></form>''')
    if fname == 'contact.dc.html':
        src = src.replace('<form aria-label="Contact form"', '<form name="contact" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="bot-field" aria-label="Contact form"')
        src = src.replace('<button type="button" style="grid-column: 1 / -1; justify-self: start;', '<input type="hidden" name="form-name" value="contact"><p hidden><label>Leave empty <input name="bot-field"></label></p><button type="submit" style="grid-column: 1 / -1; justify-self: start;')
        for lab, nm in [('Name<input type="text"', 'name'), ('Phone<input type="tel"', 'phone'), ('Email<input type="email"', 'email'), ('I am interested in<input type="text"', 'interest')]:
            src = src.replace(lab, lab + f' name="{nm}"', 1)
        src = src.replace('Message<textarea rows="5"', 'Message<textarea name="message" rows="5"')
    return src

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'assets'))
    urls = []
    for fname, src in FILES.items():
        page = convert(fname, src)
        u = url_for(fname)
        d = os.path.join(OUT, u.strip('/'))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w') as f:
            f.write(page)
        if fname != 'photo-checklist.dc.html':
            urls.append(u)
    shutil.copy(os.path.join(HERE, 'static', 'scheduler.js'), os.path.join(OUT, 'assets', 'scheduler.js'))
    shutil.copy(os.path.join(HERE, 'static', 'og-image.png'), os.path.join(OUT, 'assets', 'og-image.png'))
    with open(os.path.join(OUT, 'assets', 'favicon.svg'), 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#4A1F28"/><text x="32" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="36" fill="#F7F0EC">B</text></svg>')
    # thanks page
    thanks = FILES['contact.dc.html']
    with open(os.path.join(HERE, 'static', 'thanks.html')) as f:
        tpl = f.read()
    os.makedirs(os.path.join(OUT, 'thanks'))
    with open(os.path.join(OUT, 'thanks', 'index.html'), 'w') as f:
        f.write(tpl)
    with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                ''.join(f'  <url><loc>{SITE_URL}{u}</loc></url>\n' for u in sorted(urls)) + '</urlset>\n')
    with open(os.path.join(OUT, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\nDisallow: /photo-checklist/\nSitemap: {SITE_URL}/sitemap.xml\n')
    print(len(FILES), 'pages ->', OUT)

if __name__ == '__main__':
    main()
