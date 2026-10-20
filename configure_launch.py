#!/usr/bin/env python3
"""Set final site URLs. Preview stays noindex unless --enable-indexing is supplied."""
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape
import argparse,json,re
parser=argparse.ArgumentParser();parser.add_argument('--site-url',required=True,help='Final HTTPS origin or GitHub Pages project URL');parser.add_argument('--enable-indexing',action='store_true');args=parser.parse_args()
base=args.site_url.rstrip('/');u=urlparse(base)
if u.scheme!='https' or not u.netloc or u.query or u.fragment or any(c in base for c in '<>"\' '):parser.error('Use a complete HTTPS website URL without query, fragment or spaces.')
root=Path(__file__).resolve().parent;dist=root/'dist' if (root/'dist/index.html').exists() else root
pages={'index.html':'','privacy.html':'privacy.html','accessibility.html':'accessibility.html'}
for filename,route in pages.items():
 p=dist/filename;s=p.read_text();url=base+'/'+route
 s=re.sub(r'<link rel="canonical"[^>]*>','',s);s=re.sub(r'<meta property="og:(?:url|image)"[^>]*>','',s)
 s=re.sub(r'<meta name="robots" content="[^"]*">','<meta name="robots" content="'+('index,follow' if args.enable_indexing else 'noindex,nofollow')+'">',s)
 s=s.replace('</head>','<link rel="canonical" href="'+url+'"><meta property="og:url" content="'+url+'"><meta property="og:image" content="'+base+'/assets/luxe-logo.png"></head>')
 if filename=='index.html':
  pattern=r'(<script id="business-schema" type="application/ld\+json">)(.*?)(</script>)';m=re.search(pattern,s);data=json.loads(m.group(2));data.update({'@id':base+'/#business','url':base+'/','image':base+'/assets/luxe-logo.png','logo':base+'/assets/luxe-logo.png'});s=s[:m.start(2)]+json.dumps(data,ensure_ascii=False)+s[m.end(2):]
 p.write_text(s)
if args.enable_indexing:
 (dist/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n')
 urls=[base+'/',base+'/privacy.html',base+'/accessibility.html'];(dist/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(x)+'</loc></url>' for x in urls)+'</urlset>\n')
else:
 (dist/'robots.txt').write_text('User-agent: *\nDisallow: /\n');(dist/'sitemap.xml').unlink(missing_ok=True)
p=dist/'404.html';s=p.read_text();s=re.sub(r'<base href="[^"]*">','',s);s=s.replace('</head>','<base href="'+base+'/" ></head>');p.write_text(s)
(dist/'launch-status.json').write_text(json.dumps({'site_url':base,'indexing_enabled':args.enable_indexing},indent=2))
print('Configured',base,'| indexing', 'enabled' if args.enable_indexing else 'disabled')
