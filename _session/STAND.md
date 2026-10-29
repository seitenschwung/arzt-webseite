# Arzt-Webseite Dr. med. Christoph Manicke: Stand (28.10.2026)

Repo: `git@github.com:Nirnberger/arzt-webseite.git` (privat). Statische Seite (HTML/CSS/JS, keine Build-Tools nötig).
Commits als `Nirnberger <philipp.nirnberger@gmail.com>`.

## Branches

| Branch | Inhalt | Letzter Commit |
|---|---|---|
| `redesign-n26-stil` (Standard) | Version 2, Stil N26/Gyn Paradeplatz, Porträt, Mockup unter `mockup/mockup-v2.*` | 175284a Mockup von Version 2 |
| `v3-wirbelsaeule-motiv` | Version 3, Wirbelsäulen-Motiv, interaktive Wirbelsäule im Hero, Mockup unter `mockup/` | 8d29776 Interaktive Wirbelsäule im ersten Bildschirm |
| `hero-split-reveal` (von `redesign-n26-stil`) | v2 mit geteiltem Hero, der die v3-Wirbelsäule freilegt, plus Scroll-Übergänge. Committet, nicht gepusht. | 1bf87d7 Geteilter Hero mit Wirbelsäule und Scroll-Übergänge |

Beide Branches sind gepusht, Arbeitsverzeichnis sauber. Aktuell ausgecheckt: `redesign-n26-stil`.

## Branch `hero-split-reveal`: Stand 28.10.2026 abends

Committet als 1bf87d7 (29.10.2026), noch nicht gepusht.

### Was drin ist (Reihenfolge auf der Seite)

1. **Hero mit geteilten Türen** (`.split`, 340svh, sticky): Die obere weiße Hälfte geht nach oben, die untere Teal-Hälfte nach unten und gibt `.sp-hero` mit der Wirbelsäule frei.
   - Überschrift „Jeder Wirbel zählt.“ Vor der h1 steht „Zweite Meinung zur Wirbelsäule:“ nur für Screenreader (`.sr-only`).
   - Die Fakten-Kacheln und die Infobox „Wo tut es weh?“ sind entfernt.
   - Einblend-Animationen laufen verzögert nach dem Öffnen (`is-open`).
2. **Zoom in einen Wirbel:** Der Wirbel nahe der Bildschirmmitte füllt den Bildschirm mit Teal, danach gleitet die Seite bis zu „Erst verstehen, dann entscheiden.“.
   - `DIVE_SNAP = 0.06` hat eine andere Sitzung gesetzt: Der Zoom startet fast sofort.
3. **Intro** („Erst verstehen…“) ist Teal mit runden unteren Ecken. Darunter liegt die `.cartilage`-Bandscheibe (Mint-Polster auf Papier), dann „Wobei ich berate“ (`.deal`, runde obere Ecken).
4. **Zoom-out entfernt (29.10.2026):** Die liegende Wirbelsäule (`.zoomout`, Wirbel-Fakten `VERTEBRAE`, Überblendung aus „Wobei ich berate“) ist auf Wunsch des Nutzers raus. Nach der letzten Karte scrollt „Wobei ich berate“ normal zu „Zeit für Ihre Fragen“. Backup vor dem Entfernen: Scratchpad `index.before-zo-removal.html`, sonst aus diesem Abschnitt der Datei-Historie rekonstruieren.
5. „Zeit für Ihre Fragen“ (`.practice`), FAQ, Kontakt, Footer: unverändert.

Entfernt: die Sektion „So läuft die Zweitmeinung“ (`.steps`, Menüpunkt „Ablauf“).

### Technik

- **`glider`** (globales Objekt im Skript): eine gemeinsame Auto-Gleitfahrt für alle Szenen.
  - Ab 30 % läuft eine Szene allein zu Ende (Hermite-Kurve, übernimmt das Scrolltempo).
  - Scrollen in die Gegenrichtung bricht sofort ab.
  - Gleiche Richtung wird geschluckt. Nach der Landung nach unten wird höchstens 500 ms abgefangen, nach oben gar nicht.
- **`paintBar(chapter)`** färbt die Kopfleiste. Bei überlappenden Abschnitten gewinnt der mit dem höheren z-index.
- **Reduzierte Bewegung:** Jede Szene blendet nur über, statt zu zoomen.
- **Vorschau-Hinweis:** Die Browser-Vorschau der App zeigt `file://` als `data:`-Schnappschuss. Relative Skripte und Anker-Links gehen dort nicht. Für Tests mit externen Dateien eine Kopie unter `/private/tmp` per `python3 -m http.server` ausliefern (Desktop ist für den Server gesperrt).
- **Ausgeblendetes Fenster:** In der ausgeblendeten Vorschau ist das Fenster 0×0 und rAF gedrosselt. Mit `resize_window` eine feste Größe setzen und `window.scrollTo = () => {}` überschreiben, um Einzelbilder ohne Auto-Gleiten zu prüfen.

### Was der Nutzer verworfen hat (nicht wieder vorschlagen)

- **3D-Wirbel mit three.js:** Stilbruch, gelöscht samt `assets/vendor/`.
- **Flacher CSS-Kippwirbel**, der sich zur Draufsicht dreht: ersetzt.
- **MRT-Scanlinie** als Übergang: „scheiße“, gelöscht.
- **Leere einfarbige Seite** am Ende eines Übergangs: Er will direkt beim Text landen.

### Offene Punkte / Probleme

- [ ] Scroll-Gefühl auf einem echten Trackpad und auf iOS ist nicht getestet. Getestet wurde nur mit simuliertem Scrollen.
- [ ] Weitere Übergangsideen, noch nicht gebaut:
  - Karten werden Wirbel
  - Wirbelsäulen-Fortschrittsleiste am Rand
  - Türen links/rechts
  - Wirbel-Silhouette als Maske
  - Linienzeichnung
  - Große Schrift als Band
- [ ] Der Design-Hook meldet 8× „cramped padding“. Das war schon vor dieser Arbeit so, der Nutzer hat nicht entschieden.
- [ ] Der Design-Hook meldet geringen Kontrast bei `.motion-toggle:hover` (#7a8883). Das war ebenfalls schon vorher so.
- [ ] Die Kopfleisten-Farbe kann nach Sprung-Navigation kurz falsch sein, bis der Observer feuert.
- [ ] Unversioniert im Projekt: `Fragebogen-Dr-Manicke.pdf`, laut Fork-Sitzung eine alte Kopie, die Kopie liegt in Nextcloud.

## Was in der Session gemacht wurde

1. v1-Landingpage gebaut (taste skill), Audit mit Vercel Web Interface Guidelines, kritische/hohe Punkte behoben.
2. v2: Redesign nach README-Links (N26, gyn-paradeplatz.ch, Doctolib), echte Fakten übernommen: nur Privatpraxis, Burgstraße 2, Kiel, keine Doctolib-Buchung. Porträt `doc` eingebaut.
3. Git-Repo angelegt, v2 gepusht, ungenutztes Fjord-Video gelöscht.
4. v3 nach genehmigtem Designplan:
   - Palette Förde/Sand/Mint, Schriften Archivo + Newsreader kursiv
   - Signatur-Element: Wirbelkörper-Blöcke
   - Unsplash-Bilder, Credits im Footer
5. Mockups für v2 und v3 erstellt und auf den jeweiligen Branch gepusht.
6. Unlesbare Miniaturbilder nach dem Hero entfernt.
7. 20 alternative Headlines vorgeschlagen (5 + 15), noch keine gewählt.
8. Hero-Wirbelsäule interaktiv gemacht:
   - Der Effekt läuft dynamisch pro Wirbel (Gauß-Abfall um den Zeiger).
   - Die Infobox bleibt beim Abschnitt (HWS/BWS/LWS/ISG) und ist anklickbar, mit 420 ms Verzögerung vor dem Ausblenden.
   - Maus-Klick springt zu „Wo es wehtut“; Touch zeigt eine Vorschau, der Link in der Box springt.
   - Deep-Link `?bereich=hws|bws|lws|isg` wählt den Abschnitt und das Formularfeld vor.
   - Getestet mit Tastatur, Touch und reduzierter Bewegung.

## Wie v3 gebaut wird

`index.html` auf v3 wird erzeugt, nicht von Hand gepflegt:

- `_session/build/template.html`: Vorlage mit Platzhaltern `{{FAQ}}`, `{{SPINE_HERO}}`, `{{SPINE_MINI}}`
- `_session/build/spine.py`: erzeugt die SVG-Wirbelsäule (`interactive=True` für den Hero)
- `_session/build/build.py`: füllt die Vorlage und schreibt `index.html`. Vor dem Ausführen die Pfade im Skript prüfen; sie zeigten auf den alten Temp-Ordner.

Testskripte (CDP, nutzen `.claude/skills/design-taste-frontend/scripts/lib/cdp.mjs`, Node 22 nötig: `export PATH=/Users/deluxe/.nvm/versions/node/v22.15.0/bin:$PATH`):

- `_session/tests/shoot.mjs`, `render.mjs`: Screenshots
- `_session/tests/keys.mjs`: Fokus-Test
- `_session/tests/touch.mjs`: Touch-Test

`_session/` ist nicht committet.

## Offene Todos

- [ ] Headline auswählen (aus den 20 Vorschlägen), dann Hero-h1 in v3 ändern, prüfen, committen.
- [ ] v2-Bug: Bei 1440 px überlappt die Intro-Zeile „Drei Schritte…“ die mittlere MRT-Kachel.
- [ ] Rechtstexte ergänzen (grün markierte TODOs in `impressum.html`/`datenschutz.html`):
  - USt-ID, falls vorhanden
  - Name und Anschrift des Hosters, AV-Vertrag
  - Aufbewahrungsdauer der Server-Logs (aktuell Platzhalter 7 Tage)
  - Danach rechtlich prüfen lassen.
- [ ] Porträt in höherer Auflösung besorgen, Bildrechte klären.
- [ ] GOÄ-Abrechnungsaussage und Verwendung des Zitats mit dem Arzt bestätigen.
- [ ] Aufräumen: ungenutzte Bilder `assets/v3/kiel-harbour.webp` und `kiel-aerial.webp` (2000 px) aus dem Repo nehmen.
- [ ] Optional: Build-Skripte aus `_session/build` ins Repo übernehmen, damit v3 reproduzierbar bleibt.
- [ ] Entscheiden, welche Version (v2 oder v3) live geht, dann Hosting/Deployment.

## Web-Recherche zu Dr. Manicke (29.10.2026)

- Kein öffentlicher Lebenslauf, keine Publikationen unter „Manicke C“ gefunden, keine weiteren Porträtfotos (Verzeichnisse zeigen Platzhalter).
- Verzeichnis-Angaben (teils veraltet, widersprüchlich): Facharzt für Neurochirurgie; früher Oberarzt am St. Elisabeth-Krankenhaus Kiel (Königsweg 8); Belegarzt dort und im MVZ Lubinus (Steenbeker Weg 25); Gemeinschaftspraxis mit Dr. Martin Kneip im Neurozentrum Kiel (Holtenauer Str. 93). Die Seite nennt heute Privatpraxis Burgstraße 2.
- Doctolib-Profil blockiert automatischen Abruf (Bot-Prüfung).
- Werdegang und Fotos also direkt beim Arzt erfragen (Fragebogen-PDF).
