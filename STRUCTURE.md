```
.
├── assets/               # Source assets (for building)
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── favicon.svg
│       ├── inspirehep_logo.jpg
│       └── lhcb_logo.png
├── content/              # Source content (markdown files)
│   ├── about.md
│   ├── outreach.md
│   ├── publications.md
│   ├── talks.md
│   └── teaching.md
├── scripts/              # Build and utility scripts
│   ├── LHCb_map.py
│   └── fetch_inspire.py
└── public/               # FINAL OUTPUT - Copy this directory to CERN
    ├── assets/
    │   ├── css/
    │   │   └── style.css
    │   └── img/
    │       ├── favicon.svg
    │       ├── inspirehep_logo.jpg
    │       └── lhcb_logo.png
    ├── index.html
    ├── outreach.html
    ├── publications.html
    ├── talks.html
    └── teaching.html
```

## Deployment

To deploy to CERN's WebEOS, simply copy the entire contents of the `public/` directory to your CERN web space.
