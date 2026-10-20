# Luxe Beauty by V — v13
Static website with English/Hawaiian toggle, SEO preparation and policy drafts.

## Preview upload
Unzip and upload the contents, with index.html in the repository root. Keep the assets folder intact. For GitHub Pages, select the branch and /(root) in Settings > Pages. No build or npm installation is required. The .nojekyll file bypasses Jekyll processing.

## Indexing status: OFF
The final domain is still being chosen. noindex,nofollow and robots.txt Disallow: / deliberately remain in place. This package is for review, not search submission. Do not store private client information in a public repository.

After the final HTTPS URL is selected, Webby Wahine can run:
python3 configure_launch.py --site-url https://YOUR-FINAL-DOMAIN --enable-indexing

The command generates final canonical/social/schema URLs and sitemap.xml and enables indexing. Upload the resulting files. The URL above is an instruction example, not a chosen domain. See SEO_AND_PRIVACY_REVIEW.md for the complete launch plan and remaining owner decisions.

## Included
- Website files and all local images, fonts and original SVG icons.
- privacy.html: full current-website privacy policy draft.
- accessibility.html: full accessibility statement draft with known limitations.
- Static HTML service content, local business JSON-LD and custom 404.
- Optional click-to-load Google map; no analytics or advertising pixels added.
- configure_launch.py and SEO_AND_PRIVACY_REVIEW.md.

## Remaining approvals
Vanessa must approve the policies against her actual practices. Legal review is recommended for HIPAA applicability, future intake/consent, retention and professional requirements. No HIPAA, ADA or WCAG certification is claimed. Hawaiian copy needs fluent review. Intake forms remain inactive. Google/Bing account verification and final-domain submission are not done. Check address, prices, licenses, photo permission and the supplied La Lune webfont license.

_headers works only on supporting hosts; GitHub Pages does not apply it. Private Sites access does not carry over to GitHub Pages: a Pages deployment is normally publicly reachable even while noindex is set. noindex is not access control.
