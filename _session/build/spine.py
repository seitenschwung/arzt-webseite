import math
# One vertebral body = one rounded block: the motif of the whole page.
NAMES = {'hws': 'Halswirbelsäule', 'bws': 'Brustwirbelsäule', 'lws': 'Lendenwirbelsäule', 'isg': 'Kreuzbein und Becken'}

def spine(cls, label=None, horizontal=False, interactive=False):
    regions = [('hws', 7, 30, 72, 82), ('bws', 12, 40, 88, 124), ('lws', 5, 56, 140, 172), ('isg', 3, 44, 150, 70)]
    gap = 9
    total = sum(n * (h + gap) for _, n, h, _, _ in regions)
    W = 380
    y = 6
    out = []
    i = 0
    for name, n, h, w0, w1 in regions:
        rects = []
        y0 = y
        xs = []
        for k in range(n):
            t = (y + h / 2) / total
            x = W / 2 + 34 * math.sin(t * math.pi * 2.1 + 0.35)
            w = w0 + (w1 - w0) * (k / max(1, n - 1))
            xs += [x - w / 2, x + w / 2]
            if horizontal:
                rects.append(f'<rect class="v" style="--n:{i}" x="{y:.1f}" y="{x - w/2:.1f}" width="{h}" height="{w:.1f}" rx="{h*0.34:.1f}"/>')
            else:
                rects.append(f'<rect class="v" style="--n:{i}" x="{x - w/2:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{h*0.34:.1f}"/>')
            y += h + gap
            i += 1
        if interactive:
            # a generous, invisible hit area so the small neck vertebrae are easy to point at and tap
            a, b = min(xs) - 40, max(xs) + 40
            s, e = y0 - gap / 2, y - gap / 2
            hit = (f'<rect class="hit" x="{s:.1f}" y="{a:.1f}" width="{e - s:.1f}" height="{b - a:.1f}"/>' if horizontal
                   else f'<rect class="hit" x="{a:.1f}" y="{s:.1f}" width="{b - a:.1f}" height="{e - s:.1f}"/>')
            out.append(f'<a class="seg" href="?bereich={name}#wo" data-region="{name}" aria-label="{NAMES[name]}: typische Beschwerden ansehen">' + hit + ''.join(rects) + '</a>')
        else:
            out.append(f'<g class="seg" data-region="{name}">' + ''.join(rects) + '</g>')
    vb = f'0 0 {y:.0f} {W}' if horizontal else f'0 0 {W} {y:.0f}'
    if interactive:
        aria = ' role="group" aria-label="Wirbelsäule: Abschnitt wählen"'
    elif label:
        aria = f' role="img" aria-label="{label}"'
    else:
        aria = ' aria-hidden="true" focusable="false"'
    return f'<svg class="{cls}" viewBox="{vb}"{aria}>' + ''.join(out) + '</svg>'


if __name__ == '__main__':
    print(spine('x', interactive=True)[:600])
