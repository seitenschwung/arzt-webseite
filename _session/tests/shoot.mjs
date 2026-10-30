import { Browser, sleep } from '/Users/deluxe/Desktop/arzt-webseite/.claude/skills/design-taste-frontend/scripts/lib/cdp.mjs';
const out = process.argv[2];
const url = 'http://localhost:8123/index.html';
const b = await Browser.launch();
const shots = [
  { name: 'desk-hero', w: 1440, h: 900, dsf: 2, mobile: false, sel: null },
  { name: 'desk-wo', w: 1440, h: 900, dsf: 2, mobile: false, sel: '#wo', pick: 'lws' },
  { name: 'desk-faq', w: 1440, h: 900, dsf: 2, mobile: false, sel: '#praxis' },
  { name: 'phone-hero', w: 390, h: 844, dsf: 3, mobile: true, sel: null },
  { name: 'phone-wo', w: 390, h: 844, dsf: 3, mobile: true, sel: '.preview' },
  { name: 'phone-foot', w: 390, h: 844, dsf: 3, mobile: true, sel: '.foot' },
];
for (const s of shots) {
  const p = await b.newPage({ width: s.w, height: s.h, dsf: s.dsf, mobile: s.mobile });
  await p.goto(url, { settleMs: 2500 });
  await p.eval((sel) => {
    document.querySelectorAll('[data-reveal], .mini-spine, .blocks').forEach((e) => e.classList.add('is-in'));
    if (sel) { const el = document.querySelector(sel); const top = el.getBoundingClientRect().top + scrollY - (sel === '.preview' ? 90 : 72); window.scrollTo(0, top); }
  }, s.sel);
  await sleep(1800);
  await p.screenshot({ path: `${out}/${s.name}.png`, format: 'png' });
  await p.close();
}
await b.close();
console.log('done');
