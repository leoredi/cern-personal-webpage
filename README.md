# Federico Leo Redi personal website

Static personal academic website hosted from CERNBox/WebEOS.

## Local preview

Run a simple static server from the repository root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Deployment

This folder **is** the live web root: `~/cernbox/www`, synced by the CERNBox
desktop client to `/eos/user/f/fredi/www` and served at
<https://fredi.web.cern.ch/>. Saving a file here publishes it once the client
syncs and the webeos backends refresh, so anything placed in this folder is
public. Requirements for the site to serve: the `www` folder must be shared
with the `wwweos` service account with "Can view", and the site must be
registered in CERN Web Services. Because `.git/` syncs too, `.git/.htaccess`
(`Require all denied`, not tracked by git) keeps it off the site; a
`RedirectMatch` in a root `.htaccess` had no effect on webeos. Anything that
is not part of the site (build inputs, drafts, scratch files) belongs outside
this folder.

## Structure

- `index.html` is the main page, with six sections - research interests,
  background, teaching, outreach, news, and contact. Apart from `b2mm_2026/`
  and `zsh/`, it is the only page with content. Publications, talks, and the
  detailed record are deliberately not duplicated here; INSPIRE-HEP and the PDF
  curriculum vitae carry those.
- The News section is a short dated list (`<ul class="news">`, newest first,
  one `<time datetime="YYYY-MM-DD">` per item). Add new items at the top.
- The Teaching section lists, one line per course (the years taught follow
  it, with the number of students in brackets), only the courses Federico is
  responsible for (titolare, or teacher of
  a module inside an integrated course), all at Bergamo. Courses where he is
  tutor or teaches only part of someone else's hours are left out. Each new
  academic year goes at the end of its course's line (a new course gets a new
  line). Course titles are in `<strong>`. Finished years give the number of
  students; the current academic year gives none, so add it only once the
  year is over. Keep `&nbsp;` between a year and its bracket.
- The "Last updated" line in the homepage footer fills itself in: a small
  inline script reads `document.lastModified`, which is the `Last-Modified`
  header Apache sends (the file's save time). Every save of `index.html`
  moves the date, so never type it by hand. Without JavaScript the line stays
  hidden.
- `b2mm_2026/` is the B⁰→μ⁺μ⁻ event images page for outreach and press, linked
  from the Outreach and News sections. It uses the shared
  `assets/css/plain.css` plus a few page rules. Its `index.html` is generated
  by `build_page.py` from `page_template.html`, so edit those rather than the
  HTML; see `b2mm_2026/README.md`.
- `zsh/` is "A minimal zsh", a personal note on the zsh setup (four config
  files, written for working with AI agents; one copy for macOS and Ubuntu,
  branching on `$OSTYPE`), linked from News. It uses the
  shared `assets/css/plain.css` plus page rules in its own `<style>`.
  `zshenv`, `zprofile`, `zshrc`, and `install.sh` next to it are the
  downloads; they are shown inline in `index.html` too, so keep both in sync
  with the files in `~` when the setup changes.
- `assets/` contains shared CSS, images, and the public PDF CV. Every page
  uses `assets/css/plain.css` (Georgia, black on white, blue links, no web
  fonts); subpages add a few rules in their own `<style>`.
  `assets/css/style.css` (EB Garamond and IBM Plex Mono, section headings in
  the left margin) is the previous look and is no longer linked from any
  page. The link row under the
  masthead (`.elsewhere`) starts with an in-page link to News, then the
  external profiles, the CV, and email. The site icon is a drawn atom, shipped three ways:
  `favicon.svg` for modern browsers, `favicon.ico` as the universal fallback,
  and `apple-touch-icon.png` for iOS.
- `sideprojects/starmap/` contains the standalone star map pages and their
  images. The generator scripts and their data (ephemeris, Hipparcos
  catalogue, Milky Way EXR) live outside the web root, in
  `~/cernbox/zzz_sandbox/starmap/`.
- `sideprojects/playlists/` contains the classical playlists page and its CSV data.
- `dictee/` is an unlisted dictation site for Giulio with its own `.htaccess`
  (`noindex`).
- `two-routes-zurich/` is an unlisted page on the 29 October 2026 trip: the
  flight from Shanghai and the train from Salzburg on one map, with a replay
  of the day. Self-contained (own CSS, fonts, d3); its `.htaccess` sends
  `noindex`, and nothing links to it. See its `README.md` for data sources.
  Both unlisted folders are in `.gitignore`, so they stay out of the public
  GitHub repository.
- `internal/` is behind CERN login: its `.htaccess` requires an
  `openid-connect` session with the CERN default role. It is in `.gitignore`,
  since the GitHub repository is public.
