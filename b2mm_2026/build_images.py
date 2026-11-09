"""Make the web renditions of the renders for the outreach page (index.html).
usage: python3 build_images.py    (from this folder; reads ../b2mm_render/out)
full:  6000x4000 JPEG q92, 300 dpi (the files people download)
view:  2400x1600 JPEG q85 (lightbox)       thumb: 1200x800 JPEG q82 (grid)
Writes images.json with the pixel sizes and file sizes used by the page."""
import json, os
from PIL import Image
OUT = "../b2mm_render/out"
IMAGES = [
    # id, source png, download name
    ("c5", "LHCb_B0mumu_candidate_C5_run332869_realcalo_6000x4000.png", "LHCb_B0mumu_candidate_C5_run332869"),
    ("c5-zoom", "LHCb_B0mumu_candidate_C5_run332869_realcalo_vertexzoom_6000x4000.png", "LHCb_B0mumu_candidate_C5_run332869_vertex_closeup"),
    ("c5-white", "LHCb_B0mumu_candidate_C5_run332869_realcalo_white_6000x4000.png", "LHCb_B0mumu_candidate_C5_run332869_white"),
    ("c3", "LHCb_B0mumu_candidate_C3_run302433_ecalclusters_6000x4000.png", "LHCb_B0mumu_candidate_C3_run302433"),
    ("c3-zoom", "LHCb_B0mumu_candidate_C3_run302433_ecalclusters_vertexzoom_6000x4000.png", "LHCb_B0mumu_candidate_C3_run302433_vertex_closeup"),
    ("c3-white", "LHCb_B0mumu_candidate_C3_run302433_ecalclusters_white_6000x4000.png", "LHCb_B0mumu_candidate_C3_run302433_white"),
    ("c4", "LHCb_B0mumu_candidate_C4_run308388_ecalclusters_6000x4000.png", "LHCb_B0mumu_candidate_C4_run308388"),
    ("c4-zoom", "LHCb_B0mumu_candidate_C4_run308388_ecalclusters_vertexzoom_6000x4000.png", "LHCb_B0mumu_candidate_C4_run308388_vertex_closeup"),
    ("c4-white", "LHCb_B0mumu_candidate_C4_run308388_ecalclusters_white_6000x4000.png", "LHCb_B0mumu_candidate_C4_run308388_white"),
    ("sim", "B0mumu_SIMULATED_notext_6000x4000.png", "B0mumu_SIMULATED_illustration"),
    ("sim-labelled", "B0mumu_simulated_annotated_6000x4000.png", "B0mumu_SIMULATED_illustration_labelled"),
]
for d in ("img/full", "img/view", "img/thumb"):
    os.makedirs(d, exist_ok=True)
meta = {}
for iid, src, name in IMAGES:
    im = Image.open(os.path.join(OUT, src)).convert("RGB")
    full = f"img/full/{name}_6000x4000.jpg"
    im.save(full, quality=92, subsampling=0, dpi=(300, 300), optimize=True)
    im.resize((2400, 1600), Image.LANCZOS).save(f"img/view/{iid}.jpg", quality=85, optimize=True, progressive=True)
    im.resize((1200, 800), Image.LANCZOS).save(f"img/thumb/{iid}.jpg", quality=82, optimize=True, progressive=True)
    meta[iid] = dict(full=full, filename=os.path.basename(full), mb=round(os.path.getsize(full) / 1e6, 1), w=im.width, h=im.height)
    print(iid, meta[iid]["mb"], "MB")
json.dump(meta, open("images.json", "w"), indent=1)
