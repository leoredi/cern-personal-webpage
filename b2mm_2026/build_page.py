"""Write index.html: a static HTML5 page for the B0 -> mu+ mu- event images.
usage: python3 build_page.py     (after build_images.py; reads images.json)
The page is a subpage of fredi.web.cern.ch: it uses the site's shared stylesheet (../assets/css/plain.css)
plus a few page rules, and a little JavaScript for the version switcher, the enlarged view and the copy
buttons. Without JavaScript every image and download link still works."""
import html
import json
import os

IMG = json.load(open("images.json"))
ZIP = "LHCb_B0mumu_event_images.zip"
ZIP_MB = round(os.path.getsize(ZIP) / 1e6) if os.path.exists(ZIP) else None

REAL_VERSIONS = [("", "Without text"), ("-zoom", "With vertex close-up"), ("-white", "White background")]
SIM_VERSIONS = [("", "Without text"), ("-labelled", "Labelled, with close-up")]
EVENTS = [
    dict(id="c5", name="Candidate C5", recommended=True, real=True, versions=REAL_VERSIONS,
         tags=["2025 data", "Real calorimeter cells"],
         facts=[("Run", "332869"), ("Event", "64344859789"), ("Recorded", "3 Nov 2025, 10:12 GMT"), ("m(μ⁺μ⁻)", "5255.2 MeV"), ("B⁰ flight", "10.4 mm"), ("B⁰ momentum", "52.5 GeV (7.8 GeV transverse)"), ("B⁰ decay time", "3.5 ps"), ("μ opening angle", "11.6°")],
         drawn="Drawn from the data: the two muons and their chamber pads, the other tracks, energy in both calorimeters and all 424 muon-chamber hits of the event.",
         caption="A candidate B⁰ → μ⁺μ⁻ decay recorded by the LHCb experiment in November 2025. The B⁰ meson travels about 1 cm before decaying into two muons (pink), which cross the whole detector. Blue lines are other particles produced in the same proton–proton collision; amber and teal show energy deposited in the calorimeters."),
    dict(id="c3", name="Candidate C3", real=True, versions=REAL_VERSIONS,
         tags=["2024 data", "Widest muon opening"],
         facts=[("Run", "302433"), ("Event", "6948609257"), ("Recorded", "29 Jul 2024, 17:20 GMT"), ("m(μ⁺μ⁻)", "5285.9 MeV"), ("B⁰ flight", "12.6 mm"), ("B⁰ momentum", "56.8 GeV (7.0 GeV transverse)"), ("B⁰ decay time", "3.9 ps"), ("μ opening angle", "13.2°")],
         drawn="Drawn from the data: the two muons and their chamber pads, the other tracks and the electromagnetic-calorimeter clusters reconstructed by the trigger.",
         caption="A candidate B⁰ → μ⁺μ⁻ decay recorded by the LHCb experiment in July 2024. The B⁰ meson travels about 1.3 cm before decaying into two muons (pink), which cross the whole detector. Blue lines are other particles produced in the same proton–proton collision; amber shows energy in the electromagnetic calorimeter."),
    dict(id="c4", name="Candidate C4", real=True, versions=REAL_VERSIONS,
         tags=["2024 data"],
         facts=[("Run", "308388"), ("Event", "64182699450"), ("Recorded", "13 Oct 2024, 21:51 GMT"), ("m(μ⁺μ⁻)", "5276.2 MeV"), ("B⁰ flight", "4.6 mm"), ("B⁰ momentum", "57.8 GeV (11.6 GeV transverse)"), ("B⁰ decay time", "1.4 ps"), ("μ opening angle", "12.5°")],
         drawn="Drawn from the data: the two muons and their chamber pads, the other tracks and the electromagnetic-calorimeter clusters reconstructed by the trigger.",
         caption="A candidate B⁰ → μ⁺μ⁻ decay recorded by the LHCb experiment in October 2024. The B⁰ meson travels about 5 mm before decaying into two muons (pink), which cross the whole detector. Blue lines are other particles produced in the same proton–proton collision; amber shows energy in the electromagnetic calorimeter."),
]
SIM = dict(id="sim", name="Simulated B⁰ → μ⁺μ⁻ decay", real=False, versions=SIM_VERSIONS, tags=[],
           facts=[("Collision", "Run 350489, June 2026"), ("Simulated", "B⁰ → μ⁺μ⁻ decay"), ("B⁰ flight", "8.5 mm")],
           drawn="The two pink muons are simulated, with the correct B⁰ mass and kinematics, and bent in the magnetic field. Everything else is a real collision from the LHCb live event display.",
           caption="Visualisation of a B⁰ → μ⁺μ⁻ decay in the LHCb detector. The decay is simulated; the other particles come from a real proton–proton collision recorded by LHCb in 2026.")

e = html.escape


def rich(s):
    """Escape, then set the superscripts as <sup> and keep the decay on one line."""
    s = e(s).replace("B⁰ → μ⁺μ⁻", '<span class="nw">B⁰ → μ⁺μ⁻</span>')
    return s.replace("⁰", "<sup>0</sup>").replace("⁺", "<sup>+</sup>").replace("⁻", "<sup>−</sup>")


def event_html(ev):
    first = ev["id"] + ev["versions"][0][0]
    tags = []
    if ev.get("recommended"):
        tags.append('<li class="rec">Recommended</li>')
    tags.append('<li>Real data</li>' if ev["real"] else '<li class="sim">Not a recorded decay</li>')
    tags += [f'<li>{rich(t)}</li>' for t in ev["tags"]]
    variants = "\n".join(
        f'          <button class="variant" type="button" aria-pressed="{"true" if i == 0 else "false"}" data-img="{ev["id"]}{s}" data-label="{e(lab)}">'
        f'<img src="img/thumb/{ev["id"]}{s}.jpg" alt="" loading="lazy" width="1200" height="800">{e(lab)}</button>'
        for i, (s, lab) in enumerate(ev["versions"]))
    facts = "\n".join(f"              <dt>{rich(k)}</dt><dd>{rich(v)}</dd>" for k, v in ev["facts"])
    downloads = "\n".join(
        f'              <li><a class="dl{" current" if i == 0 else ""}" data-img="{ev["id"]}{s}" href="{IMG[ev["id"] + s]["full"]}" download>'
        f'<span class="dl-name">{e(lab)}</span><span class="dl-meta">JPEG · {IMG[ev["id"] + s]["mb"]} MB</span></a></li>'
        for i, (s, lab) in enumerate(ev["versions"]))
    simnote = ('            <p class="simnote"><strong>Simulation.</strong> The caption must say this is a visualisation, '
               'not a recorded B<sup>0</sup> decay.</p>\n') if not ev["real"] else ""
    return f"""      <article class="event" id="{ev['id']}" aria-labelledby="{ev['id']}-h">
        <figure class="plate">
          <a class="stage" href="img/view/{first}.jpg" data-title="{e(ev['name'])}" aria-label="Enlarge {e(ev['name'])}">
            <img src="img/view/{first}.jpg" alt="{e(ev['name'])}, {e(ev['versions'][0][1].lower())}" width="2400" height="1600"{'' if ev.get('recommended') else ' loading="lazy"'}>
            <span class="zoomhint">Enlarge</span>
          </a>
          <div class="variants" role="group" aria-label="Versions of {e(ev['name'])}">
{variants}
          </div>
        </figure>
        <div class="entry">
          <div class="entry-head">
            <h3 id="{ev['id']}-h">{rich(ev['name'])}</h3>
            <ul class="tags">{''.join(tags)}</ul>
          </div>
          <div class="prose">
            <dl class="facts">
{facts}
            </dl>
{simnote}            <p class="drawn">{rich(ev['drawn'])}</p>
            <div class="caption">
              <span class="label">Suggested caption</span>
              <p class="captext" data-copy="{e(ev['caption'])}">{rich(ev['caption'])}</p>
              <p><button class="textbtn copy" type="button">Copy caption</button><span class="status" aria-live="polite"></span></p>
            </div>
            <span class="label">Download · 6000 × 4000 px · 300 dpi</span>
            <ul class="dls">
{downloads}
            </ul>
          </div>
        </div>
      </article>"""


zip_link = (f'<li><a href="{ZIP}" download>Download all images</a> <span class="meta">ZIP · {len(IMG)} files · {ZIP_MB} MB</span></li>'
            if ZIP_MB else "")
page = open("page_template.html", encoding="utf-8").read()
page = (page.replace("{{REAL}}", "\n".join(event_html(ev) for ev in EVENTS))
            .replace("{{SIM}}", event_html(SIM))
            .replace("{{ZIP}}", zip_link))
open("index.html", "w", encoding="utf-8").write(page)
print("wrote index.html")
