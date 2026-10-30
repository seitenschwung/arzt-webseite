import { Browser, sleep } from '/Users/deluxe/Desktop/arzt-webseite/.claude/skills/design-taste-frontend/scripts/lib/cdp.mjs';
const b = await Browser.launch();
for (const [w, h, mobile] of [[1440, 900, false], [390, 844, true]]) {
  const p = await b.newPage({ width: w, height: h, dsf: 1, mobile });
  await p.goto('http://localhost:8123/index.html', { settleMs: 2500 });
  // real keyboard focus: tab until a spine section is focused
  const res = await p.eval(async () => {
    const seg = [...document.querySelectorAll('.hero-spine .seg, .hero-spine-h .seg')].find((s) => s.getBoundingClientRect().width > 0 && s.dataset.region === 'hws');
    seg.focus();
    await new Promise((r) => setTimeout(r, 400));
    const tip = document.querySelector('.spine-tip');
    return { focused: document.activeElement === seg, tip: tip.querySelector('b').textContent, shown: tip.classList.contains('is-shown') || getComputedStyle(tip).opacity, hot: [...document.querySelectorAll('.seg.is-hot')].map((x) => x.dataset.region).join(','), hasFocus: document.hasFocus() };
  });
  console.log(w, JSON.stringify(res));
  await p.screenshot({ path: `/private/tmp/claude-501/-Users-deluxe--claude-spares-spare-OqXXN1/93260805-0d17-48d6-851c-9fa580010b6d/scratchpad/mock/focus-${w}.png`, format: 'png' });
  await p.close();
}
await b.close();
