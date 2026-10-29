import { Browser, sleep } from '/Users/deluxe/Desktop/arzt-webseite/.claude/skills/design-taste-frontend/scripts/lib/cdp.mjs';
const [,, url, out] = process.argv;
const b = await Browser.launch({ width: 3200, height: 2000 });
const p = await b.newPage({ width: 3200, height: 2000, dsf: 1 });
await p.goto(url, { settleMs: 2000 });
await sleep(800);
await p.screenshot({ path: out, format: 'png' });
await b.close();
console.log('ok');
