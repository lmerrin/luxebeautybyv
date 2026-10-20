# Luxe Beauty by V — SEO, privacy and intake review
Prepared October 19, 2026 · Webby Wahine · Website v13

## Status
The final domain is still being chosen. The review site and this package deliberately retain noindex,nofollow and robots.txt Disallow: /. They are not ready to be submitted for indexing. There is no ranking or indexing guarantee. The documents are complete drafts for the website as configured, not a certification of legal compliance. Vanessa should approve them and have counsel review applicability to her actual business and record handling.

## Implemented
- A descriptive English title targeting esthetician services in Kamuela (Waimea), Hawaiʻi Island, with an existing Hawaiian title when selected.
- Visible local service context, readable headings, links and service descriptions; brand H1 preserved.
- All nine advertised service rows in initial HTML. JavaScript filters these rows; content and booking links remain usable without JavaScript.
- BeautySalon JSON-LD with name, address, phone, email, founder and nine service offers. No unverified reviews, ratings, hours, coordinates or license claims added.
- Open Graph title/description and social-card type. Final canonical, social URL/image and schema identity are generated when the final domain is known.
- A custom 404 page. Relative asset paths support GitHub Pages project paths.
- Self-hosted DM Sans and Italiana font files in addition to the supplied La Lune font, reducing third-party font requests.
- Google Maps changed to click-to-load; no map request until a visitor selects Load map. Written address and external directions link remain available.
- Fully written privacy.html and accessibility.html pages, linked in the footer. These pages remain in English for owner/legal review; Hawaiian link labels identify English content.
- Visible focus states, semantic controls, alt text, keyboard navigation and reduced-motion support retained. Selected code-level behavior checks performed. A comprehensive assistive-technology audit and performance audit remain outstanding.
- Existing security-header file retained. GitHub Pages ignores _headers; those response headers require a supporting host. HTTPS and redirect behavior must be verified on the actual final domain.

## Final-domain launch sequence
1. Register the domain in Vanessa’s/business’s name, in her own account with MFA and renewal details. Decide www versus non-www and redirect the other host to the preferred version. Do not publish the same indexable site at multiple hosts.
2. Confirm final address, treatment prices, booking links, email, owner credentials, hours and photo-publication permissions. The Square page previously listed two locations; confirm the active address before final launch.
3. Approve policies and Hawaiian editorial copy. Confirm the provided La Lune font’s web-use license.
4. Run configure_launch.py against the final HTTPS URL with --enable-indexing. This sets canonical and social URLs, updates business identity, generates sitemap.xml and allows crawling. It works from this repository or from the extracted GitHub package.
5. Upload the resulting site files to the final hosting repository, enforce HTTPS, verify the redirects and inspect the delivered robots.txt and page robots tag. A noindex page must be crawlable for Google to see noindex; neither robots blocking nor noindex is an access-control mechanism. Keep private material out of every public code repository.
6. Add the final domain to Google Search Console in Vanessa’s account, verify by DNS, submit sitemap.xml, and inspect/request indexing for the homepage. Add Bing Webmaster Tools as well. These account actions were not performed here.
7. Validate the final page in Google’s Rich Results Test and PageSpeed Insights. Check mobile layout, keyboard-only use, 200%/400% zoom, a screen reader, forms when introduced, contrast, 404 response and all Square links on the final domain. No field Core Web Vitals score is claimed.
8. Monitor Search Console coverage and search queries, booking inquiries and broken links over the following weeks. Update copy based on actual customer questions rather than repeating location keywords.

To configure: python3 configure_launch.py --site-url https://YOUR-FINAL-DOMAIN --enable-indexing
The URL above is an instruction example, not a registered or selected domain. Webby Wahine can run this after Vanessa chooses her address.

## What helps local rankings
Google says local results depend mainly on relevance, distance and prominence. A website cannot control how far away a searcher is. A verified, accurate Google Business Profile is a priority: correct category, name, salon address/suite, service list, hours, booking link and original photos. Keep name/address/phone consistent across the website, Square and legitimate listings. Ask real customers for honest reviews without incentives or selective review gating; respond without disclosing private treatment information. Seek relevant local links such as an approved salon listing or community/business listing. Avoid paid-link schemes, invented reviews, keyword-stuffed business names and doorway pages for locations she does not serve.

After the simple landing page is approved, useful dedicated service pages may help visitors compare microblading, brow styling, lash lifts, facials and waxing. Each needs substantive owner-approved details: what it is, whom it is for, what to expect, preparation, aftercare, duration and price. Do not invent clinical claims, guarantees, credentials or contraindications. A blog is not required merely for SEO.

## Hawaiian language and search
The current toggle changes one URL using local browser storage. It helps visitors but does not provide separately indexable Hawaiian URLs. After fluent-language approval, consider a real Hawaiian page and reciprocal hreflang links. Do not add hreflang pointing to identical pages or claim the existing toggle creates a second indexed language version. Keep Square’s recognizable treatment names where needed for clear booking.

## HIPAA: determine whether it applies first
Being an esthetician, collecting allergies or taking card payments does not by itself establish HIPAA-covered status. HHS applies HIPAA to covered entities and business associates; healthcare providers are covered only when they conduct the relevant standard electronic transactions, or another covered definition applies. Business-associate relationships involving PHI can also matter. This review cannot determine Vanessa’s status from public pages. Ask whether she submits insurance/standard healthcare transactions, works for a covered medical practice, or receives/maintains PHI on a covered entity’s behalf. Counsel should assess the actual arrangement. Do not advertise the site as HIPAA compliant or publish a HIPAA Notice of Privacy Practices merely because she provides beauty services.

The public site has no active intake form and stores no submitted client health records. HTTPS, a signature field, Google Drive, or a vendor’s compliance marketing do not establish end-to-end compliance. If HIPAA applies, every relevant provider and integration must be assessed, required BAAs executed, access controls configured, and operational policies implemented. Google’s guidance requires applicable Workspace services plus an accepted BAA; a personal account is not a substitute for that arrangement. Jotform offers HIPAA-enabled accounts, but the account, plan, settings and integration path must be verified. Do not assume a basic Square or Jotform account automatically covers every health-data workflow.

## Recommended future intake workflow
Use a form/signature platform in Vanessa’s own business account and a clearly labeled Client forms page or secure link sent with booking instructions. Build from her approved forms rather than generating unreviewed treatment-consent language. Use separate service-specific consent where appropriate. Ask only for information necessary for the actual service. Explain why sensitive questions are asked. Keep optional marketing/photo permission separate from treatment consent; record permission for each proposed use.

Preferred data flow: client opens approved hosted form → completes questions and signature → protected provider record/PDF → restricted business storage if an approved integration is used → email notification that a form is ready. Avoid putting completed health histories in ordinary email attachments, email subject lines, analytics, URLs or GitHub. Keep signature/audit evidence and identify the consent version/date. Vanessa should choose the retention/deletion schedule with her insurer/counsel and confirm requirements for minors and each service. Test the complete workflow with fictitious records, including failed delivery, access revocation and deletion, before collecting real information.

Use individual accounts, MFA, least-privilege sharing, restricted Drive folders and protected devices. Avoid shared passwords and public link sharing. Define who reviews submitted contraindication information; a submitted form is not clinical clearance. Provide contact alternatives without requesting medical details through an unsecured channel. Prepare an incident-response process and review Hawaii breach-notification requirements if relevant personal information is involved. FTC consumer-protection obligations can matter even outside HIPAA; its Health Breach Notification Rule covers certain non-HIPAA entities, not automatically every salon.

For the PMU/microblading services, confirm licensing, facility permits, consent and sanitation requirements with Hawaii DCCA and Department of Health as appropriate. This report does not verify Vanessa’s licenses or determine that an esthetics license alone authorizes all listed services. A general website disclaimer does not replace required professional permissions, treatment screening, aftercare or service-specific consent.

## Privacy and accessibility drafts: owner checks
The policy describes current website features: no active forms/payments, no installed advertising/analytics tracker, local language preference, hosting technical logs, locally served fonts/photos, optional Google map and external links. Confirm this against actual hosting/account settings and real inquiry handling. Update the policy BEFORE adding analytics, pixels, newsletter tools, intake, storage integrations or new recipients. A cookie banner is not added as a cosmetic compliance feature; assess consent requirements for actual tools and jurisdictions.

The accessibility statement sets WCAG 2.2 AA as an aim, lists present features, discloses incomplete testing and gives a contact route. It does not declare ADA/WCAG compliance. A statement or overlay alone does not make a website accessible. Physical salon access remains unverified and should be described only after confirmation. Policies are not a substitute for implementing the practices described.

## Sources checked October 19, 2026
- Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google local ranking: https://support.google.com/business/answer/7091
- Local business structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- JavaScript SEO: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- Multilingual websites: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- HHS covered entities: https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html
- HHS business associates: https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html
- Google Workspace HIPAA guidance: https://knowledge.workspace.google.com/admin/compliance/hipaa-compliance-with-google-workspace-and-cloud-identity
- Jotform HIPAA-enabled forms: https://www.jotform.com/hipaa/
- DOJ web accessibility: https://www.ada.gov/resources/web-guidance/
- Hawaii breach notices: https://cca.hawaii.gov/ocp/notices/security-breach/
- FTC health information guidance: https://www.ftc.gov/business-guidance/resources/collecting-using-or-sharing-consumer-health-information-look-hipaa-ftc-act-health-breach
- Hawaii license verification: https://cca.hawaii.gov/pvl/request-for-a-license-verification/
