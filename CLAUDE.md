# Projekt: Praxis-Webseite Dr. med. Christoph Manicke (Neurochirurg, Kiel)

Statische Seite (HTML/CSS/JS inline, kein Build, kein Bundler) plus kleiner Node-Mailer für das Anfrageformular.
Live: https://christophmanicke.de (Coolify). Texte deutsch, Code-Kommentare englisch.

## Wo liegt was
- `index.html` (~840 Zeilen): die ganze Seite, CSS und JS inline (Wirbelsäule, Scroll-Szenen, FAQ, Kontaktformular).
- `impressum.html`, `datenschutz.html` (+ `assets/legal.css`), `robots.txt`, `sitemap.xml`.
- `fancy/index.html`: Variante der Seite, wird mit ausgeliefert (Dockerfile prüft sie).
- `assets/`: Bilder/Fonts/Video. `assets/credits.json` = Lizenzdaten; Bildnachweis steht in `index.html#bildnachweis`.
- `mailer/`: `server.mjs` (HTTP, Port 3000), `lib.mjs` (Validierung/Mail), Tests `*.test.mjs`; einzige Dependency nodemailer (gepinnt).
- `nginx.conf`: Port 8080, `/healthz`, `/version.txt`, Weiterleitung www/alt -> Hauptdomain, `/api/anfrage` -> Mailer (5 Req/min).
- `Dockerfile`, `docker-compose.yml` (`web` + `mailer`), `.github/workflows/ci.yml` (dünner Aufruf von `seitenschwung/template`).
- `README.md`: Deploy/SMTP-Setup für den Owner. `_session/`, `.taste-skill/`, `.agents/`, `graphify-out/`, `mockup/`: Altlasten
  früherer Sitzungen (z. B. `_session/tests/*.mjs` haben absolute Mac-Pfade), nicht anfassen. `doc/` ist gitignored.

## Befehle (geprüft)
- Dev: `python3 -m http.server 8123 --bind 0.0.0.0` im Repo-Root, dann `/index.html` (200). Kein npm im Root (`package.json` fehlt).
  Preview des Owners: `$PREVIEW_URL` (niedrigster Port). Das Formular braucht den Mailer nicht (Fallback: Mailprogramm).
- Mailer-Tests: `cd mailer && npm ci --no-audit --no-fund && node --test *.test.mjs` (50 Tests, ~1 s).
- Mailer lokal: `node mailer/server.mjs`; Env: `SMTP_HOST/PORT/USER/PASS`, `MAIL_FROM`, `MAIL_TO`, `ALLOWED_ORIGINS`.
  Ohne `SMTP_PASS` antwortet er 503.
- Bauen/Image: `docker build --target test .` (Tests + Prüfung, dass kein Patientenbild ausgeliefert wird). Docker gibt es in der
  Sandbox nicht (nicht ausprobiert): CI läuft es.
- Deploy: kein manueller Schritt. Push auf `main` -> CI (`ci_wait`) -> Image nach ghcr.io -> Coolify (`DEPLOY=auto`), mit Rollback.
  Prüfen: `deploy_status`. Workflow-Dateien nur über `request_workflow_push`.

## Git / Branches
- Standard-Branch des Repos ist `redesign-n26-stil` (alt), aber PRs gehen gegen `main`: `gh pr create --base main`.
  Neue Branches von `origin/main`. Ein Task = ein Branch = ein PR, Squash-Merge (Titel endet auf `(#N)`).
- Commit-Messages deutsch, ein Satz, Thema vorn ("Beratung: ...", "Wirbelsäule: ...", "Kontaktformular: ...").
- Branch `claude/issue-N` bei Issue-Aufgaben.

## Konventionen und Stolperstellen
- Nur Bilder, deren Dateiname in `index.html`, `impressum.html`, `datenschutz.html` oder `fancy/index.html` vorkommt, landen im Image
  (Dockerfile löscht den Rest). Neue Asset-Namen also in einer Seite referenzieren.
- Nie `assets/v2/l4-l5-disc-herniation.png` (Patientendaten) oder Dateien mit `herniation`/`sagittal` im Namen ausliefern; der Test-Stage schlägt sonst fehl.
- Neue Bilder: `.webp` (bei großen Fotos mehrere Breiten wie `-800/-1200/-1600`), Lizenz in `assets/credits.json` und im Bildnachweis ergänzen.
- Datenschutz/Impressum müssen zu Formularfeldern passen (neues Feld: Formular, `mailer/lib.mjs`, Tests, `datenschutz.html` zusammen ändern).
- Texte sind Kundenangaben des Arztes: Wortlaut nicht frei umschreiben; neue/geänderte Texte gehen mit `manual-review`.
- Compose: Variable ohne Default in `SMTP_PASS` ist Absicht (Coolify schreibt sonst den Wert nicht). Container sind read-only, `cap_drop: ALL`,
  Logs via journald (14 Tage, im Datenschutz zugesagt). CrowdSec-Labels (`nginx`) bleiben.
- Compose-Kommentar verweist auf README "Log retention": diesen Abschnitt gibt es dort nicht (Host-Setup liegt beim Owner).
- Scroll-Szenen und Wirbelsäule sind empfindlich (Sticky-Höhen in `svh`, gemeinsamer Scroll-Handler): nach Änderungen Desktop 1280x800
  und Mobil 390x844 im Browser prüfen, auch `prefers-reduced-motion`.
- CI testet axe + Lighthouse: Kontraste, Alt-Texte, Überschriften-Reihenfolge nicht verschlechtern.
