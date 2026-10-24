# Website Dr. med. Christoph Manicke – Neurochirurgie Kiel

Statische One-Page-Website (reines HTML/CSS, kein Build-Schritt, kein JavaScript).

## Dateien

```
index.html                  Die komplette Website (Styles inline bzw. im <head>)
images/portrait-manicke.webp Porträtfoto (aus dem Doctolib-Profil, Rand beschnitten)
README.md                   Diese Datei
```

Lokal ansehen: `index.html` im Browser öffnen.
Veröffentlichen: den Ordner unverändert auf einen beliebigen Webspace / statisches Hosting
(z. B. Coolify, Netlify, GitHub Pages, nginx) laden.

## Externe Ressourcen

- Schrift **Manrope** über Google Fonts. Für DSGVO-konformen Betrieb besser lokal einbinden
  (z. B. über google-webfonts-helper herunterladen und per `@font-face` laden).
- **Wirbelsäulen-Foto** wird direkt von Unsplash geladen
  (Foto: Julius Toltesi, https://unsplash.com/photos/5thrMBqG5E0). Für den Live-Betrieb
  herunterladen, als `images/wirbelsaeule.jpg` ablegen und den `src` in `index.html` anpassen.

## Praxisdaten (Quelle: Doctolib-Profil)

- Herr Dr. med. Christoph Manicke, Facharzt für Neurochirurgie
- Burgstraße 2, 24103 Kiel – 4. Stock mit Aufzug
- Sprechstunde nach Vereinbarung · Tel. 0172 6347706 · christoph.manicke@gmx.de
- Nur privat Versicherte oder Selbstzahlende · keine Online-Buchung
- Schwerpunkt Wirbelsäulenerkrankungen; konservatives und operatives Behandlungsspektrum,
  Zweitmeinung, Beratung nach Operationen

## Design

- Inspiration: n26.com (reduziert, Pillen-Buttons, große Rundungen) und gyn-paradeplatz.ch (Aufbau)
- Farben: Petrol `#16695F`, dunkles Petrol `#0E4A43`, Mint `#E3F0EC`, Grau `#F3F6F5` / `#F7F9F8`,
  Text `#111614`, Fließtext `#3E4744`
- Aufbau: Header → Hero mit Wirbelsäulen-Foto (Porträt unter „Über mich“) → 4 Info-Kacheln → Leistungen → Über mich → FAQ → Kontakt → Footer
- Responsiv: unter 760 px wird die Navigation ausgeblendet, Bereiche stapeln sich

## Offene Punkte

- [ ] Impressum und Datenschutzerklärung erstellen (Pflicht in Deutschland); Footer-Links zeigen noch auf `#`
- [ ] Porträt als Originaldatei von Dr. Manicke anfordern, Bildrechte klären
- [ ] Wirbelsäulen-Foto (jetzt Hero-Header) und Schrift lokal einbinden (siehe oben)
- [ ] Werdegang (Abschnitt „Über mich“) mit echten Angaben füllen – aktuell Platzhalter
- [ ] Logo (derzeit Monogramm „CM“)
- [ ] Domain und Hosting festlegen
