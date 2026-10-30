import sys
sys.path.insert(0, '.')
from spine import spine
t = open('template.html').read()
faq = [
 ('Wer', 'Wer kann in die Sprechstunde kommen?', 'Die Praxis ist eine Privatpraxis für privat Versicherte und Selbstzahler. Gesetzlich Versicherte können als Selbstzahler kommen.'),
 ('Termin', 'Wie bekomme ich einen Termin?', 'Nach Vereinbarung, telefonisch unter 0172&nbsp;6347706 oder per E-Mail an christoph.manicke@gmx.de. Eine Online-Buchung gibt es nicht.'),
 ('Kosten', 'Was kostet eine Zweitmeinung?', 'Abgerechnet wird nach der Gebührenordnung für Ärzte (GOÄ). Ob Ihre Versicherung die Kosten übernimmt, klären Sie am besten vorher mit ihr.'),
 ('Unterlagen', 'Was soll ich mitbringen?', 'Ihre aktuellen MRT- oder CT-Bilder auf CD oder als Link, Arztbriefe und Befunde, die schriftliche OP-Empfehlung, falls es eine gibt, und eine Liste Ihrer Medikamente.'),
 ('Nach der OP', 'Ich bin schon operiert. Kann ich trotzdem kommen?', 'Ja. Auch nach einer bereits durchgeführten Operation ist eine Beratung möglich, etwa wenn Beschwerden geblieben oder neu aufgetreten sind.'),
 ('Anfahrt', 'Ist die Praxis barrierefrei erreichbar?', 'Die Praxis liegt im 4.&nbsp;Stock der Burgstraße&nbsp;2 und ist mit einem Aufzug erreichbar.'),
]
cols = [('#f7f7f5', None), ('#c0e2bf', None), ('#5d6c67', '#f7f7f5')]
out = []
for i, (tab, q, a) in enumerate(faq):
    c, ci = cols[i % 3]
    style = f'--i:{i}; --c:{c}' + (f'; --ci:{ci}' if ci else '')
    out.append(f'<article class="fcard" style="{style}"><span class="tab" aria-hidden="true">{tab}</span><button type="button" aria-expanded="false" aria-controls="fa-{i}"><span class="q">{q}</span></button><p class="answer" id="fa-{i}">{a}</p></article>')
t = t.replace('{{FAQ}}', '\n        '.join(out))
t = t.replace('{{SPINE_HERO}}', spine('hero-spine', interactive=True) + spine('hero-spine-h', horizontal=True, interactive=True))
t = t.replace('{{SPINE_MINI}}', spine('mini-spine', 'Schema der Wirbelsäule mit Hals-, Brust- und Lendenwirbelsäule und Kreuzbein'))
open('/Users/deluxe/Desktop/arzt-webseite/index.html', 'w').write(t)
print('built', len(t))
