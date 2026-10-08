#!/usr/bin/env python3
"""Build compact markdown reference files from the GSoC organizations dataset.

Usage: python scripts/build_gsoc.py [--input orgs.json] [--out references/gsoc]
"""
import argparse
import html
import json
import os
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import date

URL = "https://api.gsocorganizations.dev/organizations.json"

ALIASES = {
    "cpp": "c++", "c plus plus": "c++", "cplusplus": "c++",
    "js": "javascript", "ecmascript": "javascript",
    "ts": "typescript",
    "node": "node.js", "nodejs": "node.js", "node js": "node.js",
    "golang": "go", "go lang": "go",
    "reactjs": "react", "react.js": "react", "react js": "react",
    "vuejs": "vue", "vue.js": "vue", "angularjs": "angular",
    "py": "python", "python3": "python", "python 3": "python",
    "csharp": "c#", "c sharp": "c#",
    "ml": "machine learning", "ai": "artificial intelligence",
    "postgres": "postgresql", "k8s": "kubernetes",
    "html5": "html", "css3": "css", "objective c": "objective-c",
    "reactnative": "react native", "ror": "ruby on rails", "rails": "ruby on rails",
}
LANGS = ["python", "javascript", "typescript", "java", "c++", "c", "go", "rust",
         "c#", "php", "ruby", "kotlin", "swift", "r", "julia", "haskell"]
NOISE = {"", "none", "null", "n/a", "na", "other", "others", "etc", "-"}


def clean(text, n=0):
    if text is None:
        return ""
    s = str(text)
    s = re.sub(r"<[^>]*>", " ", s)
    s = html.unescape(s)
    s = s.replace("|", "/").replace("\r", " ").replace("\n", " ").replace("\t", " ")
    s = re.sub(r"\s+", " ", s).strip()
    if n and len(s) > n:
        s = s[:n - 3].rstrip() + "..."
    return s


def norm_tech(t):
    s = clean(t).lower().strip(" .,;:")
    s = re.sub(r"\s+", " ", s)
    s = ALIASES.get(s, s)
    return "" if s in NOISE else s


def lst(v):
    return v if isinstance(v, list) else []


def load(path):
    if path:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    req = urllib.request.Request(URL, headers={"User-Agent": "build_gsoc.py/1.0 (placement-prep skill)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def ranges(years):
    ys = sorted(years)
    out, i = [], 0
    while i < len(ys):
        j = i
        while j + 1 < len(ys) and ys[j + 1] == ys[j] + 1:
            j += 1
        out.append(str(ys[i]) if i == j else "%d-%d" % (ys[i], ys[j]))
        i = j + 1
    return ",".join(out)


def prep(raw):
    orgs = []
    for o in raw:
        if not isinstance(o, dict):
            continue
        name = clean(o.get("name"), 80)
        if not name:
            continue
        yrs = {}
        for y, d in (o.get("years") or {}).items():
            if not str(y).isdigit() or not isinstance(d, dict):
                continue
            projs = [p for p in lst(d.get("projects")) if isinstance(p, dict)]
            try:
                k = int(d.get("num_projects") or 0)
            except (TypeError, ValueError):
                k = 0
            k = max(k, len(projs))
            if k > 0:
                yrs[int(y)] = {"k": k, "titles": [clean(p.get("title"), 70) for p in projs if clean(p.get("title"))]}
        techs, seen = [], set()
        for t in lst(o.get("technologies")) + lst(o.get("topics")):
            nt = norm_tech(t)
            if nt and nt not in seen:
                seen.add(nt)
                techs.append(nt)
        ntech, seen = [], set()
        for t in lst(o.get("technologies")):
            nt = norm_tech(t)
            if nt and nt not in seen:
                seen.add(nt)
                ntech.append(nt)
        orgs.append({
            "name": name, "cat": clean(o.get("category"), 60) or "Uncategorized",
            "techs": techs, "only_tech": ntech, "years": yrs,
            "link": clean(o.get("ideas_url")) or clean(o.get("guide_url")) or clean(o.get("url")),
        })
    return orgs


def header(today, title):
    return ("<!-- Generated from api.gsocorganizations.dev by scripts/build_gsoc.py on %s; re-run yearly -->\n# %s\n\n"
            % (today, title))


def build_directory(orgs, today):
    freq = Counter(t for o in orgs for t in o["techs"])
    out = [header(today, "GSoC organizations directory")]
    out.append("Legend: `Name | tech | yrs N (years participated) | latest <year>: <k> projects | ideas: <link>`. "
               "\"yrs N\" = number of GSoC years the org participated in (ranges shown compactly). "
               "Tech = up to 6 most common technologies. Orgs active in 2025/2026 get an `e.g.` line with sample project titles. "
               "Orgs are sorted per category by years participated (desc), then name.\n")
    cats = defaultdict(list)
    for o in orgs:
        if o["years"]:
            cats[o["cat"]].append(o)
    n = 0
    for cat in sorted(cats, key=str.lower):
        out.append("## %s\n" % cat)
        for o in sorted(cats[cat], key=lambda o: (-len(o["years"]), o["name"].lower())):
            pool = o["only_tech"] or o["techs"]
            tech = ", ".join(sorted(pool, key=lambda t: (-freq[t], t))[:6]) or "-"
            ly = max(o["years"])
            k = o["years"][ly]["k"]
            out.append("%s | %s | yrs %d (%s) | latest %d: %d project%s | ideas: %s" % (
                o["name"], tech, len(o["years"]), ranges(o["years"]), ly, k, "" if k == 1 else "s", o["link"] or "-"))
            if ly >= 2025 and o["years"][ly]["titles"]:
                out.append('  e.g. ' + "; ".join('"%s"' % t for t in o["years"][ly]["titles"][:2]))
            n += 1
        out.append("")
    return "\n".join(out), n


def build_tech(orgs, today):
    by = defaultdict(set)
    for i, o in enumerate(orgs):
        for t in o["techs"]:
            by[t].add(i)

    def active(i):
        return any(y in orgs[i]["years"] for y in (2024, 2025, 2026))

    def fmt(i):
        o = orgs[i]
        return "%s (yrs %d, last %d)" % (o["name"], len(o["years"]), max(o["years"]))

    def order(ids):
        return sorted(ids, key=lambda i: (-len(orgs[i]["years"]), orgs[i]["name"].lower()))

    secs = []
    for t, ids in by.items():
        if len(ids) < 3:
            continue
        secs.append((t, order([i for i in ids if active(i)])))
    secs.sort(key=lambda s: (-len(s[1]), s[0]))
    out = [header(today, "GSoC organizations by technology")]
    out.append("Orgs active in at least one of 2024-2026, sorted by years participated (max 25 per tech). "
               "Terms are normalized (c++/cpp, js/javascript, node/node.js, golang/go, reactjs/react merged); "
               "terms used by fewer than 3 orgs overall are omitted.\n")
    out.append("## Language quick picks\n")
    out.append("| Language | Top active orgs (2024-2026) |\n|---|---|")
    d = dict(secs)
    for l in LANGS:
        if d.get(l):
            out.append("| %s | %s |" % (l, ", ".join(orgs[i]["name"] for i in d[l][:8])))
    out.append("")
    n = set()
    for t, act in secs:
        if not act:
            continue
        out.append("## %s (%d orgs active 2024-2026)\n" % (t, len(act)))
        out.append(", ".join(fmt(i) for i in act[:25]) + "\n")
        n.update(act[:25])
    return "\n".join(out), len(n)


def build_year(orgs, today):
    allyears = sorted({y for o in orgs for y in o["years"]}, reverse=True)
    first = {i: min(o["years"]) for i, o in enumerate(orgs) if o["years"]}
    out = [header(today, "GSoC organizations by year")]
    out.append("Per year: orgs grouped by category with (number of projects), then orgs new that year.\n")
    seen = set()
    for y in allyears:
        ids = [i for i, o in enumerate(orgs) if y in o["years"]]
        P = sum(orgs[i]["years"][y]["k"] for i in ids)
        out.append("## %d - %d orgs, %d projects\n" % (y, len(ids), P))
        cats = defaultdict(list)
        for i in ids:
            cats[orgs[i]["cat"]].append(i)
        for c in sorted(cats, key=str.lower):
            ls = sorted(cats[c], key=lambda i: (-orgs[i]["years"][y]["k"], orgs[i]["name"].lower()))
            out.append("**%s**: %s\n" % (c, ", ".join("%s (%d)" % (orgs[i]["name"], orgs[i]["years"][y]["k"]) for i in ls)))
            seen.update(ls)
        if y != min(allyears):
            new = sorted((orgs[i]["name"] for i in ids if first[i] == y), key=str.lower)
            out.append("New that year: %s\n" % (", ".join(new) if new else "none"))
    return "\n".join(out), len(seen)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input")
    ap.add_argument("--out", default="references/gsoc")
    a = ap.parse_args()
    orgs = prep(load(a.input))
    today = date.today().isoformat()
    os.makedirs(a.out, exist_ok=True)
    for fn, fnc in (("orgs-directory.md", build_directory), ("by-technology.md", build_tech), ("by-year.md", build_year)):
        text, n = fnc(orgs, today)
        p = os.path.join(a.out, fn)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text.rstrip() + "\n")
        print("%s: %d bytes, %d orgs" % (p, os.path.getsize(p), n))


if __name__ == "__main__":
    main()
