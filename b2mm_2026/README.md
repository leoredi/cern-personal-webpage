# B⁰→μ⁺μ⁻ event images: static web page

Plain HTML5 + CSS, with a few lines of JavaScript for the version switcher, the enlarged view and the
copy buttons. Without JavaScript every image and download still works. The page is a subpage of the
personal site: it uses the site's shared stylesheet (`../assets/css/plain.css`, Georgia, no web
fonts) and icons, and is linked from the Outreach section of `../index.html`.

- `index.html`: the page (generated, do not edit by hand)
- `img/full/`: the 6000 × 4000 px JPEGs people download; `img/view/` (2400 px) and `img/thumb/`
  (1200 px) are for the page itself
- `LHCb_B0mumu_event_images.zip`: all full-size JPEGs in one file

It is served at <https://fredi.web.cern.ch/b2mm_2026/>. Opened from disk it works as long as it stays
inside the `www` folder, since it needs `../assets/`.

To rebuild after new renders in `../b2mm_render/out`:

    python3 build_images.py                       # JPEG renditions + images.json
    (cd img/full && zip -q -0 ../../LHCb_B0mumu_event_images.zip *.jpg)
    python3 build_page.py                         # index.html from page_template.html

Texts (captions, facts, provenance) live in `build_page.py` and `page_template.html`.
