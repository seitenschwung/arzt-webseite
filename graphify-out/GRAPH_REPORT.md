# Graph Report - arzt-webseite  (2026-10-28)

## Corpus Check
- Large corpus: 447 files · ~561,863 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 160 nodes · 219 edges · 10 communities (8 shown, 2 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 52 edges (avg confidence: 0.81)
- Token cost: 573,672 input · 0 output

## Community Hubs (Navigation)
- Landingpage UI-Komponenten
- Datenschutz & Impressum
- Kiel & Ostsee Fotos
- Scroll-Szenen & Fragebogen
- Branches & Projektstand
- MRT & Bandscheibenvorfall
- Mockup v2 & Porträt
- Historische Anatomie
- CDP-Testskripte
- Offene Freigaben Arzt

## God Nodes (most connected - your core abstractions)
1. `Landing page index.html (Dr. Manicke, Kiel)` - 11 edges
2. `Gespraechsleitfaden Markenprofil (29 questions)` - 11 edges
3. `Impressum page (legal notice)` - 10 edges
4. `Kiel` - 10 edges
5. `Datenschutz page (privacy policy)` - 9 edges
6. `Zoom-out script (place, aim, pick, nearest)` - 7 edges
7. `Version 3: spine motif, Foerde/Sand/Mint palette` - 6 edges
8. `Mockup Version 2 (3200x2000 presentation)` - 6 edges
9. `Dr. med. Christoph Manicke` - 6 edges
10. `L4/L5 disc herniation sagittal T2 fat-sat MRI in DICOM viewer screenshot` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Cover: Jeder Wirbel zaehlt. Und jede Antwort.` --semantically_similar_to--> `Split hero with doors (.split, 340svh)`  [INFERRED] [semantically similar]
  Fragebogen-Dr-Manicke.pdf → _session/STAND.md
- `Block 04 Charakter (locker, Q15-20): personal details incl. favourite vertebra` --semantically_similar_to--> `Zoom-out scene with interactive spine (.zoomout, 27 VERTEBRAE)`  [INFERRED] [semantically similar]
  Fragebogen-Dr-Manicke.pdf → _session/STAND.md
- `Gespraechsleitfaden Markenprofil (29 questions)` --conceptually_related_to--> `Project status STAND.md (28.10.2026)`  [AMBIGUOUS]
  Fragebogen-Dr-Manicke.pdf → _session/STAND.md
- `Kernfragen 9, 15, 27, 28 (headlines and quotes)` --rationale_for--> `Todo: choose headline from 20 proposals`  [INFERRED]
  Fragebogen-Dr-Manicke.pdf → _session/STAND.md
- `Gespraechsleitfaden Markenprofil (29 questions)` --references--> `Dr. med. Christoph Manicke`  [EXTRACTED]
  Fragebogen-Dr-Manicke.pdf → _session/STAND.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pinned scroll scenes sharing the glider** — index_glider, index_hero_script, index_zoomout_script [EXTRACTED 1.00]
- **Bar takes colour of the chapter beneath** — index_paintbar, index_chapter_observer, index_hero_script, index_zoomout_script, index_bar [EXTRACTED 1.00]
- **Dive into vertebra, then zoom out to lying spine** — index_hero_spine_svg, index_zoom_in_dive, index_zoom_out_reveal, index_vertebrae_data [INFERRED 0.85]
- **hero-split-reveal scroll scene sequence** — _session_stand_split_hero, _session_stand_vertebra_zoom, _session_stand_cartilage_intro, _session_stand_zoomout, _session_stand_glider [EXTRACTED 0.95]
- **Legal pages with open TODOs** — impressum_page, datenschutz_page, _session_stand_todo_legal, impressum_ust_exemption, datenschutz_hosting_todo [INFERRED 0.85]
- **Questionnaire six-block structure** — fragebogen_dr_manicke_block1, fragebogen_dr_manicke_block2, fragebogen_dr_manicke_block3, fragebogen_dr_manicke_block4, fragebogen_dr_manicke_block5, fragebogen_dr_manicke_block6 [EXTRACTED 0.95]
- **Historische Wirbelsaeulen-Anatomie-Illustrationen** — assets_muscles_and_bones_of_the_vertebral_column_image, assets_vertebrae_thirteen_figures_line_engraving_by_a_image, assets_vertebral_column_with_dissections_of_nerves_and_image [INFERRED 0.85]
- **Ostsee- und Kiel-Bildwelt** — assets_kuhlungsborn_strand_lub_2025_02_14_poster_image, assets_wintermorgen_am_eingang_zur_kieler_forde_image, assets_postcard_panorama_of_kiel_1902_image, assets_st_elisabeth_krankenhaus_am_konigsweg_8_kiel_image [INFERRED 0.75]
- **Burgstrasse Kiel then and now (1966 vs 2017)** — assets_v2_burgstra_e_kiel_2017_01_image, assets_v2_burgstra_e_kiel_2017_02_image, assets_v2_burgstra_e_kiel_38_197_image, assets_v2_burgstrasse_1966_strip_image [INFERRED 0.85]
- **Sagittal lumbar MRI sequence trio (T1, T2, STIR) of the same patient** — assets_v2_sagittal_fse_t1_mri_image, assets_v2_sagittal_frfse_t2_mri_image, assets_v2_sagittal_fast_stir_mri_image [INFERRED 0.85]
- **Disc herniation MRI examples** — assets_v2_disc_herniation_image, assets_v2_l4_l5_disc_herniation_image [INFERRED 0.75]
- **Mockup v2 composed from desktop and phone screenshots** — mockup_mockup_v2_image, mockup_src_desk_hero_image, mockup_src_phone_hero_image, mockup_src_phone_deal_image [INFERRED 0.85]
- **Kiel/Baltic decorative strips** — assets_v2_ostsee_strip_image, assets_v2_panorama_strip_image, concept_kiel [INFERRED 0.75]

## Communities (10 total, 2 thin omitted)

### Community 0 - "Landingpage UI-Komponenten"
Cohesion: 0.07
Nodes (40): Fixed top bar (.bar, nav, wordmark), Card fan (4 service cards dealt on scroll), Cartilage divider (disc between vertebra-shaped sections), Chapter IntersectionObserver (bar colour by data-bg/data-ink), Kontakt section (photo strip and request bar), Leistungen section (card fan, Wobei ich berate), CSS design tokens (paper, sand, teal, sage, mint, Archivo), Doors (door-top / door-bottom headline fields) (+32 more)

### Community 1 - "Datenschutz & Impressum"
Cohesion: 0.10
Nodes (23): Practice facts: private practice only, Burgstrasse 2 Kiel, no Doctolib booking, Todo: complete legal texts (USt-ID, hoster, log retention), Verantwortlicher: Dr. med. Christoph Manicke, Burgstrasse 2, Kiel, Data subject rights (Art. 15-21 DSGVO), Health data legal basis Art. 9(2)(h) DSGVO, Hosting provider and AV contract (TODO), Unabhaengiges Landeszentrum fuer Datenschutz Schleswig-Holstein, Contact form opens mail client (mailto), sends nothing to server (+15 more)

### Community 2 - "Kiel & Ostsee Fotos"
Cohesion: 0.17
Nodes (20): Kuehlungsborn Strand (Ostsee, Winter, Foto), Postkarte Panorama von Kiel 1902, St. Elisabeth-Krankenhaus, Koenigsweg 8, Kiel (historisches s/w-Foto), Alter Markt Kiel - summer cafe terraces under plane tree, Burgstrasse 2 Kiel facade 2017 (practice building, wide view), Burgstrasse 2 Kiel entrance 2017 (street level, wide crop), Historic b/w view over Kiel rooftops with road construction near Burgstrasse (1960s), Burgstrasse 1966 strip (cropped web version of historic b/w photo) (+12 more)

### Community 3 - "Scroll-Szenen & Fragebogen"
Cohesion: 0.13
Nodes (18): Intro and cartilage disc section, glider: shared auto-glide object, paintBar(chapter) header bar colouring, Reduced motion: crossfade only, Split hero with doors (.split, 340svh), Unbuilt transition ideas (cards become vertebrae, progress bar, side doors, mask, line drawing, big type band), Zoom into a vertebra (DIVE_SNAP 0.06), Zoom-out scene with interactive spine (.zoomout, 27 VERTEBRAE) (+10 more)

### Community 4 - "Branches & Projektstand"
Cohesion: 0.14
Nodes (18): Branch hero-split-reveal (uncommitted), Branch redesign-n26-stil (v2, default), Branch v3-wirbelsaeule-motiv (v3), v3 build pipeline (template.html, spine.py, build.py), Deep link ?bereich=hws|bws|lws|isg, Open issues on hero-split-reveal (commit, fact check, trackpad/iOS test, mobile size), Project status STAND.md (28.10.2026), CDP test scripts (shoot, render, keys, touch) (+10 more)

### Community 5 - "MRT & Bandscheibenvorfall"
Cohesion: 0.28
Nodes (13): Sagittal T2 MRI crop of lumbar spine with disc herniation, L4/L5 disc herniation sagittal T2 fat-sat MRI in DICOM viewer screenshot, Sagittal FAST STIR lumbar MRI, Sagittal FRFSE T2 lumbar MRI, Sagittal FSE T1 lumbar MRI, Disc herniation, Intervertebral disc, L4/L5 spinal level (+5 more)

### Community 6 - "Mockup v2 & Porträt"
Cohesion: 0.23
Nodes (12): Portrait of Dr. Christoph Manicke (man with glasses, black polo), Palette: Papier, Sand, Petrol, Salbei, Mint, Mint pill CTA: Termin vereinbaren 0172 6347706, Dr. med. Christoph Manicke, Hero section, N26 / Gyn Paradeplatz style, Horizontal service cards with MRI spine images, Headline straddling paper/petrol split background (+4 more)

### Community 7 - "Historische Anatomie"
Cohesion: 0.57
Nodes (7): Muscles and bones of the vertebral column (Kupferstich 1748, Tab. XVI), Historic engraving of cervical vertebrae (Tab. LIX, Pl. 100), Wirbel, dreizehn Figuren (Kupferstich, A. Bell), Wirbelsaeule mit Nerven- und Gefaesspraeparation (historische Tuschezeichnung), Halswirbelsaeule, Historische Anatomie-Illustration, Wirbelsaeule

## Ambiguous Edges - Review These
- `Project status STAND.md (28.10.2026)` → `Gespraechsleitfaden Markenprofil (29 questions)`  [AMBIGUOUS]
  Fragebogen-Dr-Manicke.pdf · relation: conceptually_related_to

## Knowledge Gaps
- **50 isolated node(s):** `N26 and Gyn Paradeplatz style guides`, `Pill button (.pill)`, `Phone menu (nav-toggle)`, `Doors (door-top / door-bottom headline fields)`, `Photo strip (Kiel images, drift, motion-toggle)` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 54 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Dr. med. Christoph Manicke` connect `Datenschutz & Impressum` to `Scroll-Szenen & Fragebogen`, `Branches & Projektstand`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Kiel` (e.g. with `St. Elisabeth-Krankenhaus, Koenigsweg 8, Kiel (historisches s/w-Foto)` and `Kieler Schloss - 1960s brick and stone postwar building, cloudy sky`) actually correct?**
  _`Kiel` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `N26 and Gyn Paradeplatz style guides`, `Pill button (.pill)`, `Phone menu (nav-toggle)` to the rest of the system?**
  _50 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Landingpage UI-Komponenten` be split into smaller, more focused modules?**
  _Cohesion score 0.07051282051282051 - nodes in this community are weakly interconnected._
- **Why does `Gespraechsleitfaden Markenprofil (29 questions)` connect `Scroll-Szenen & Fragebogen` to `Datenschutz & Impressum`, `Branches & Projektstand`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Should `Datenschutz & Impressum` be split into smaller, more focused modules?**
  _Cohesion score 0.10276679841897234 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Project status STAND.md (28.10.2026)` and `Gespraechsleitfaden Markenprofil (29 questions)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._