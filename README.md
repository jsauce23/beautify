# Beautified Studios website

Live site files are in `site/` and deploy to Netlify as-is (no build step).

## Deploy on Netlify
1. Netlify > Add new site > Import from GitHub > `jsauce23/beautify`
2. Leave build command empty. Publish directory is set by `netlify.toml` (`site`).
3. Forms: Netlify picks up the `booking` and `contact` forms automatically. Turn on email notifications under Site settings > Forms so booking requests go to Brandy.

## Change the domain
The domain is set in one place: `SITE_URL` at the top of `tools/convert.py` (used for canonical links, schema and the sitemap). Change it, run `python3 tools/convert.py`, and push.

## Editing pages
All pages are generated. Edit content in `tools/build.py` (services, areas, FAQ, blog posts, photo checklist), then run:

    python3 tools/convert.py

Booking widget: `tools/static/scheduler.js`.

## Pages
Home, Treatments, 10 treatment pages, Areas we serve + 6 area pages, About, Academy, FAQ, Blog + 3 posts, Contact, Book, Thanks, and a hidden Photo checklist (noindex).
