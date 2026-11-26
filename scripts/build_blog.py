import json, html, os, sys

ROOT = sys.argv[1]
U = "https://belvedere-gastro-pub.vercel.app"
DATE = "2026-11-26"
DATE_RO = "26 noiembrie 2026"
IMG = "https://www.pensiuneabelvedere.ro/img/background-desktop.jpg"

CTA = """
<aside class="cta">
  <h3>Vii în zona Târgu Neamț?</h3>
  <p>La Belvedere Gastro Pub &amp; Pensiune ai masa și cazarea în același loc: restaurant deschis zilnic până la 22:00, camere Deluxe cu mic dejun inclus și parcare gratuită, la 3,6 km de Cetatea Neamț.</p>
  <div class="cta-actions">
    <a class="btn btn-accent" href="tel:+40747295151">📞 Sună: 0747 295 151</a>
    <a class="btn btn-wa" href="https://wa.me/40747295151?text=Bun%C4%83%20ziua!%20A%C8%99%20dori%20o%20rezervare%20la%20Belvedere." target="_blank" rel="noopener">💬 WhatsApp</a>
    <a class="btn btn-outline" href="/#cazare">Vezi camerele</a>
  </div>
</aside>
"""

ARTICLES = [
 {
  "slug": "ce-sa-vizitezi-in-targu-neamt",
  "title": "Ce să vizitezi în Târgu Neamț: ghid de weekend (1–2 zile)",
  "desc": "Ghid practic pentru un weekend în Târgu Neamț: Cetatea Neamț, Casa Ion Creangă, mănăstirile din zonă, unde mănânci și unde dormi.",
  "tag": "Ghid",
  "read": 6,
  "body": """
<p class="intro">Târgu Neamț este unul dintre cele mai frumoase orașe mici din Moldova: are o cetate medievală, casa copilăriei lui Ion Creangă și, la mică distanță, câteva dintre cele mai cunoscute mănăstiri din țară. Mai jos găsești un plan simplu pentru un weekend, cu tot ce merită văzut.</p>

<h2>Ziua 1: istorie și povești în oraș</h2>
<h3>Dimineața: Cetatea Neamț</h3>
<p>Începe cu <strong>Cetatea Neamț</strong>, ridicată pe un deal deasupra orașului încă din secolul al XIV-lea. Este una dintre cele mai importante cetăți medievale din Moldova și astăzi funcționează ca muzeu. Urcarea de la parcare se face pe jos, pe o alee în pantă, așa că ia încălțăminte comodă. De sus ai o priveliște frumoasă peste oraș și dealurile din jur.</p>
<p><em>Sfat:</em> mergi dimineața devreme, mai ales vara și în weekend, ca să eviți aglomerația. Programul și prețul biletelor se pot schimba de la un sezon la altul, așa că verifică-le înainte de vizită.</p>

<h3>Prânzul</h3>
<p>După cetate, o masă bună e binevenită. Dacă alegi Belvedere, în timpul săptămânii, între 12:00 și 15:00, ai <strong>meniul zilei</strong>. Oaspeții noștri recomandă cel mai des <strong>șnițelul Belvedere</strong>, specialitatea casei, și ciorba dreseală, o rețetă locală.</p>

<h3>După-amiaza: Casa memorială Ion Creangă din Humulești</h3>
<p>Humuleștiul, satul din <em>Amintiri din copilărie</em>, face astăzi parte din Târgu Neamț. Casa în care a copilărit Ion Creangă a devenit muzeu: o casă țărănească tradițională, mică și autentică, în care parcă îl vezi pe Nică pe cuptor. Vizita durează cam o oră și e potrivită și pentru copii.</p>

<h2>Ziua 2: mănăstirile din jurul Târgu Neamțului</h2>
<p>A doua zi merită dedicată mănăstirilor. Cele mai cunoscute sunt la mai puțin de jumătate de oră cu mașina:</p>
<ul>
  <li><strong>Mănăstirea Agapia</strong> (aprox. 14 km): biserica are picturi realizate de tânărul Nicolae Grigorescu.</li>
  <li><strong>Mănăstirea Văratec</strong> (aprox. 15 km): una dintre cele mai mari mănăstiri de maici din țară, într-un cadru liniștit.</li>
  <li><strong>Mănăstirea Neamț</strong>: una dintre cele mai vechi și importante mănăstiri din Moldova.</li>
</ul>
<p>Am scris un articol separat despre <a href="/blog/manastirile-agapia-si-varatec.html">traseul Agapia – Văratec</a>, cu sfaturi practice.</p>

<h2>Unde dormi</h2>
<p>Pentru un weekend, cel mai comod e să stai într-un loc de unde ajungi repede peste tot. Pensiunea Belvedere este pe Str. Mărășești 215, la 3,6 km de Cetatea Neamț, are parcare privată gratuită și mic dejun inclus. Despre ce merită să urmărești când alegi cazarea, citește <a href="/blog/cazare-langa-cetatea-neamt.html">ghidul nostru de cazare lângă Cetatea Neamț</a>.</p>

<h2>Pe scurt</h2>
<ul>
  <li><strong>Ziua 1:</strong> Cetatea Neamț, prânz, Casa Ion Creangă.</li>
  <li><strong>Ziua 2:</strong> Agapia, Văratec și Mănăstirea Neamț.</li>
  <li><strong>Ia cu tine:</strong> încălțăminte comodă și haine potrivite pentru mănăstiri (umeri și genunchi acoperiți).</li>
</ul>
""",
  "faq": [
   ("Cât timp îți trebuie pentru Târgu Neamț?", "Un weekend de 1–2 zile e suficient pentru Cetatea Neamț, Casa Ion Creangă și mănăstirile Agapia, Văratec și Neamț."),
   ("Ce poți vizita gratuit în Târgu Neamț?", "Te poți plimba prin oraș și pe dealul cetății, iar curțile mănăstirilor din zonă se pot vizita de obicei fără bilet. Pentru muzee, verifică prețurile actualizate înainte."),
  ],
 },
 {
  "slug": "cum-ajungi-la-cetatea-neamt",
  "title": "Cum ajungi la Cetatea Neamț și ce trebuie să știi înainte de vizită",
  "desc": "Întrebări frecvente despre Cetatea Neamț: cum ajungi, cât durează vizita, când e cel mai bine să mergi și ce faci după.",
  "tag": "Întrebări",
  "read": 4,
  "body": """
<p class="intro">Cetatea Neamț este principalul obiectiv turistic din Târgu Neamț. Am adunat răspunsurile la întrebările pe care ni le pun cel mai des oaspeții înainte să urce la cetate.</p>

<h2>Unde se află Cetatea Neamț?</h2>
<p>Cetatea este pe un deal din partea de vest a orașului Târgu Neamț, în județul Neamț. Se vede din mai multe puncte ale orașului, iar indicatoarele te duc ușor până la parcarea de la baza dealului. De la Belvedere (Str. Mărășești 215) sunt aproximativ <strong>3,6 km</strong>, adică doar câteva minute cu mașina.</p>

<h2>Cum urci până la cetate?</h2>
<p>Din parcare se urcă pe jos, pe o alee în pantă, iar la final intri în cetate pe un pod. Urcarea durează în jur de 10–15 minute în ritm lejer. Nu e dificilă, dar e în pantă, așa că încălțămintea comodă e obligatorie. Pentru persoanele cu mobilitate redusă, urcarea poate fi solicitantă.</p>

<h2>Cât durează vizita?</h2>
<p>Pentru cetate în sine, socotește <strong>1–2 ore</strong>, cu tot cu urcarea, turul curții interioare, sălile cu exponate și pozele de pe ziduri.</p>

<h2>Când e cel mai bine să mergi?</h2>
<ul>
  <li><strong>Dimineața devreme</strong>, ca să eviți grupurile organizate și căldura de vară.</li>
  <li><strong>Primăvara și toamna</strong>, când dealurile din jur sunt cele mai frumoase.</li>
  <li><strong>În timpul săptămânii</strong>, dacă vrei liniște.</li>
</ul>
<p>Programul și prețurile biletelor se pot schimba de la un sezon la altul, așa că verifică-le pe surse oficiale înainte de vizită.</p>

<h2>Merită să mergi cu copiii?</h2>
<p>Da. Zidurile, podul și curtea interioară îi impresionează pe cei mici, iar povestea cetății se leagă de lecțiile de istorie despre Ștefan cel Mare. Ține copiii aproape pe porțiunile de pe ziduri.</p>

<h2>Ce faci după vizită?</h2>
<p>Combină cetatea cu <strong>Casa memorială Ion Creangă</strong> din Humulești, tot în Târgu Neamț. Apoi oprește-te la o masă: la Belvedere găsești bucătărie românească și internațională, porții generoase și terasă. Dacă vrei să rămâi mai mult în zonă, vezi și <a href="/blog/ce-sa-vizitezi-in-targu-neamt.html">ghidul nostru de weekend în Târgu Neamț</a>.</p>
""",
  "faq": [
   ("Cât de departe e Cetatea Neamț de Belvedere?", "Aproximativ 3,6 km, adică câteva minute cu mașina."),
   ("Cât durează vizita la Cetatea Neamț?", "În jur de 1–2 ore, cu tot cu urcarea de la parcare, care durează 10–15 minute."),
   ("Este greu de urcat la Cetatea Neamț?", "Nu e dificil, dar aleea e în pantă. Încălțămintea comodă e recomandată."),
  ],
 },
 {
  "slug": "cazare-langa-cetatea-neamt",
  "title": "Cazare lângă Cetatea Neamț: cum alegi pensiunea potrivită",
  "desc": "Ce să verifici când cauți cazare în Târgu Neamț: locație, parcare, mic dejun, recenzii și animale de companie. Plus ce oferă Pensiunea Belvedere.",
  "tag": "Cazare",
  "read": 5,
  "body": """
<p class="intro">Dacă vii la Cetatea Neamț sau la mănăstirile din zonă, alegerea cazării contează la fel de mult ca traseul. Iată ce merită să verifici înainte să rezervi o pensiune în Târgu Neamț.</p>

<h2>1. Locația: aproape de tot, dar liniștit</h2>
<p>Ideal e să fii la câteva minute de cetate și de centru, dar într-o zonă liniștită, unde dormi bine. Uită-te pe hartă la distanța față de obiectivele care te interesează: Cetatea Neamț, Humulești, Agapia, Văratec.</p>
<p><em>La Belvedere:</em> suntem la 3,6 km de Cetatea Neamț și la 14–15 km de mănăstirile Agapia și Văratec, la marginea orașului, aproape de centru.</p>

<h2>2. Parcare inclusă</h2>
<p>În zonă ai nevoie aproape sigur de mașină, ca să ajungi la mănăstiri. Verifică dacă pensiunea are parcare proprie și dacă e gratuită.</p>
<p><em>La Belvedere:</em> parcare privată gratuită, în curtea pensiunii.</p>

<h2>3. Micul dejun și restaurantul</h2>
<p>După o zi de drumeții, e mult mai simplu să ai restaurantul la parter. Întreabă dacă micul dejun e inclus și ce variante are.</p>
<p><em>La Belvedere:</em> mic dejun inclus, iar restaurantul, un gastro pub cu bucătărie românească și internațională, e deschis zilnic până la 22:00.</p>

<h2>4. Recenziile recente</h2>
<p>Citește recenziile din ultimele luni, nu doar nota generală. Urmărește ce spun oaspeții despre curățenie, personal și mâncare.</p>
<p><em>La Belvedere:</em> nota 9,1 din 10 pe Booking.com, din peste 530 de evaluări. Pe Booking, personalul are 9,5, iar curățenia 9,4.</p>

<h2>5. Camere și facilități</h2>
<p>Verifică tipul de pat, dacă ai baie proprie și dacă primești extra-uri mici care contează, precum cafeaua în cameră sau un Wi-Fi bun.</p>
<p><em>La Belvedere:</em> camere duble Deluxe cu balcon și camere twin Deluxe, cu baie proprie, TV, aparat de cafea și ceai și Wi-Fi gratuit. Multe au vedere la grădină.</p>

<h2>6. Călătorești cu animalul de companie?</h2>
<p>Nu toate pensiunile acceptă animale, iar unele percep taxe suplimentare.</p>
<p><em>La Belvedere:</em> animalele de companie sunt binevenite, fără taxe suplimentare.</p>

<h2>7. Bonus: sustenabilitate</h2>
<p>Tot mai mulți turiști aleg cazări care au grijă de mediu. Pensiunea Belvedere are certificarea europeană <strong>EU Ecolabel</strong>.</p>

<h2>Check-list rapid</h2>
<ul>
  <li>Distanța până la Cetatea Neamț și mănăstiri</li>
  <li>Parcare gratuită</li>
  <li>Mic dejun inclus și restaurant pe loc</li>
  <li>Recenzii recente bune</li>
  <li>Politica pentru animale de companie</li>
  <li>Ora de check-in și check-out (la Belvedere: 15:00 / 12:00)</li>
</ul>
""",
  "faq": [
   ("Pensiunea Belvedere include micul dejun?", "Da, micul dejun este inclus pentru oaspeții pensiunii."),
   ("Pensiunea Belvedere acceptă animale de companie?", "Da, animalele de companie sunt acceptate fără taxe suplimentare."),
   ("La ce distanță e Pensiunea Belvedere de Cetatea Neamț?", "La aproximativ 3,6 km."),
  ],
 },
 {
  "slug": "manastirile-agapia-si-varatec",
  "title": "Mănăstirile Agapia și Văratec: traseu de o zi din Târgu Neamț",
  "desc": "Cum vizitezi mănăstirile Agapia și Văratec într-o singură zi, plecând din Târgu Neamț: distanțe, ce să vezi, ce să porți și sfaturi practice.",
  "tag": "Traseu",
  "read": 5,
  "body": """
<p class="intro">Agapia și Văratec sunt două dintre cele mai frumoase mănăstiri de maici din Moldova și se pot vizita ușor în aceeași zi, plecând din Târgu Neamț. Iată cum să-ți organizezi traseul.</p>

<h2>Distanțe din Târgu Neamț</h2>
<ul>
  <li><strong>Belvedere → Mănăstirea Agapia:</strong> aproximativ 14 km</li>
  <li><strong>Belvedere → Mănăstirea Văratec:</strong> aproximativ 15 km</li>
</ul>
<p>Drumul durează în jur de 20–25 de minute cu mașina până la fiecare dintre ele, iar cele două mănăstiri sunt aproape una de alta.</p>

<h2>Mănăstirea Agapia</h2>
<p>Agapia este cunoscută mai ales pentru <strong>pictura bisericii mari</strong>, realizată de tânărul <strong>Nicolae Grigorescu</strong>, înainte să devină unul dintre cei mai mari pictori români. Complexul e mare, cu chilii albe, flori și ateliere ale maicilor. Socotește cel puțin o oră pentru vizită.</p>

<h2>Mănăstirea Văratec</h2>
<p>Văratec este una dintre cele mai mari mănăstiri de maici din țară, așezată într-un cadru liniștit, la marginea pădurii. Mulți vizitatori se opresc și la mormântul poetei <strong>Veronica Micle</strong>, înmormântată aici. E un loc bun pentru o plimbare lungă și liniștită.</p>

<h2>Traseu propus</h2>
<ol>
  <li><strong>Dimineața:</strong> mic dejun și plecare spre Agapia.</li>
  <li><strong>Până la prânz:</strong> vizită la Agapia.</li>
  <li><strong>După-amiaza:</strong> Văratec și o plimbare prin împrejurimi.</li>
  <li><strong>Seara:</strong> întoarcere în Târgu Neamț pentru cină.</li>
</ol>

<h2>Ce să porți</h2>
<p>La mănăstiri, ținuta trebuie să fie decentă: umerii și genunchii acoperiți. Femeile poartă de obicei fustă și eșarfă pe cap; la intrare se găsesc uneori fuste sau eșarfe de împrumut. Ia și încălțăminte comodă, pentru că vei merge destul de mult pe jos.</p>

<h2>Sfaturi practice</h2>
<ul>
  <li>Respectă liniștea și regulile fiecărei mănăstiri. În interiorul bisericilor, fotografiatul poate fi interzis.</li>
  <li>Ia bani cash pentru lumânări și pentru produsele făcute de maici.</li>
  <li>Evită zilele de mari sărbători dacă nu vrei aglomerație; vino tocmai atunci dacă vrei să prinzi slujbele.</li>
</ul>

<h2>Unde te întorci seara</h2>
<p>După o zi pe drumuri, o cină caldă și un pat bun fac toată diferența. La Belvedere te așteptăm cu restaurantul deschis până la 22:00 și camere cu mic dejun inclus. Pentru mai multe idei, vezi <a href="/blog/ce-sa-vizitezi-in-targu-neamt.html">ce să vizitezi în Târgu Neamț</a>.</p>
""",
  "faq": [
   ("Se pot vizita Agapia și Văratec în aceeași zi?", "Da. Ambele sunt la aproximativ 14–15 km de Târgu Neamț și aproape una de alta."),
   ("Ce ținută se cere la mănăstirile Agapia și Văratec?", "Umerii și genunchii acoperiți. Femeile poartă de obicei fustă și eșarfă pe cap."),
  ],
 },
 {
  "slug": "ce-sa-mananci-in-targu-neamt",
  "title": "Ce să mănânci în Târgu Neamț: preparate moldovenești de încercat",
  "desc": "Preparate tradiționale moldovenești pe care merită să le încerci în Târgu Neamț și recomandările bucătăriei Belvedere Gastro Pub.",
  "tag": "Gastronomie",
  "read": 4,
  "body": """
<p class="intro">Moldova e cunoscută pentru mâncarea ei îmbelșugată: ciorbe acrite cu borș, carne gătită încet, smântână și mămăligă. Dacă ajungi în Târgu Neamț, iată ce merită să guști.</p>

<h2>Preparate moldovenești clasice</h2>
<h3>Ciorbele</h3>
<p>În Moldova, ciorbele se acresc tradițional cu <strong>borș</strong> și se servesc cu smântână și ardei iute. Merită încercate ciorba de văcuță și ciorbele locale, făcute după rețete transmise din generație în generație.</p>
<h3>Sarmalele cu mămăliguță</h3>
<p>Nelipsite de la mesele de sărbătoare, sarmalele moldovenești sunt de obicei mai mici, în foi de varză murată sau de viță-de-vie, și se servesc cu mămăliguță și smântână.</p>
<h3>Tochitura moldovenească</h3>
<p>Carne de porc prăjită în sos, servită cu mămăligă, brânză și ou ochi. E o masă consistentă, perfectă după o zi de drumeții.</p>
<h3>Papanașii</h3>
<p>Desertul care încheie orice masă în Moldova: gogoși din brânză de vaci, cu smântână și dulceață de afine sau vișine.</p>

<h2>Ce recomandă bucătăria Belvedere</h2>
<p>La Belvedere Gastro Pub combinăm bucătăria românească cu cea internațională. Iată ce aleg cel mai des oaspeții noștri:</p>
<ul>
  <li><strong>Șnițelul Belvedere</strong>, specialitatea casei</li>
  <li><strong>Ciorba dreseală</strong>, o rețetă locală</li>
  <li><strong>Ciorba de văcuță</strong></li>
  <li><strong>Coastele de porc</strong></li>
  <li><strong>Burgerul gourmet</strong>, mai ales joia, la <strong>Joia burgerilor</strong></li>
  <li><strong>Humusul și opțiunile vegane</strong>, pentru cine vrea ceva mai ușor</li>
</ul>
<p>De luni până vineri, între 12:00 și 15:00, avem și <strong>meniul zilei</strong>. Dimineața, oaspeții pensiunii au mic dejun inclus, cu platou de mezeluri afumate și clătite pufoase.</p>

<h2>Unde ne găsești</h2>
<p>Belvedere Gastro Pub, Str. Mărășești 215, Târgu Neamț. Restaurantul e deschis zilnic, până la 22:00. Pentru rezervări sau comenzi, sună la <a href="tel:+40747295151">0747 295 151</a>.</p>
""",
  "faq": [
   ("Ce preparate tradiționale să încerc în Târgu Neamț?", "Ciorbe acrite cu borș, sarmale cu mămăliguță, tochitură moldovenească și papanași."),
   ("Care este specialitatea casei la Belvedere?", "Șnițelul Belvedere. Oaspeții recomandă și ciorba dreseală, o rețetă locală."),
   ("Belvedere are meniul zilei?", "Da, de luni până vineri, între 12:00 și 15:00."),
  ],
 },
]

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles_batch2 import ARTICLES2
from articles_batch3 import ARTICLES3
HIDDEN = ARTICLES2 + ARTICLES3
VISIBLE = list(ARTICLES)          # listed on /blog/ (batch 1)
ARTICLES = ARTICLES + HIDDEN    # batch 2 is 'backend': only sitemap, llms.txt and links between batch-2 articles

HEAD = """<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="ro_RO">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.bunny.net">
<link href="https://fonts.bunny.net/css?family=oswald:400,500,600|inter:400,500,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/blog/blog.css">
{ld}
</head>
<body>
<header class="top"><div class="wrap nav">
  <a href="/" class="brand">Belvedere<small>Gastro Pub &amp; Pensiune</small></a>
  <nav><a href="/blog/">Blog</a><a href="/#meniu">Meniu</a><a href="/#cazare">Cazare</a><a href="/#contact" class="btn btn-accent">Rezervă</a></nav>
</div></header>
"""

FOOT = """
<footer><div class="wrap foot">
  <span class="brand">Belvedere</span>
  <span>© 2026 Belvedere Gastro Pub &amp; Pensiune · Str. Mărășești 215, Târgu Neamț · <a href="tel:+40747295151">0747 295 151</a></span>
  <span><a href="/politica-confidentialitate.html">Confidențialitate</a> · <a href="https://www.facebook.com/BelvederePensiuneRestaurant/" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/belvedere.gastrohan/" target="_blank" rel="noopener">Instagram</a></span>
</div></footer>
</body>
</html>
"""

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=1) + '\n</script>'

os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
publisher = {"@type": "Organization", "name": "Belvedere Gastro Pub & Pensiune", "url": U + "/"}

for a in ARTICLES:
    url = f"{U}/blog/{a['slug']}.html"
    graph = [
      {"@type": "BlogPosting", "headline": a["title"], "description": a["desc"], "image": IMG,
       "datePublished": DATE, "dateModified": DATE, "inLanguage": "ro-RO",
       "author": publisher, "publisher": publisher, "mainEntityOfPage": url},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Acasă", "item": U + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": U + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
    ]
    faq_html = "\n".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(ans)}</p></details>" for q, ans in a["faq"])
    summary_html = f'<div class="summary"><b>Pe scurt</b><p>{html.escape(a["summary"])}</p></div>' if a.get("summary") else ""
    pool = VISIBLE if a in VISIBLE else HIDDEN
    i = pool.index(a)
    others = [pool[(i + k) % len(pool)] for k in (1, 2, 3)]
    related = "\n".join(f'<a class="rel" href="/blog/{o["slug"]}.html"><span>{o["tag"]}</span>{html.escape(o["title"])}</a>' for o in others)
    page = HEAD.format(title=html.escape(a["title"]) + " | Belvedere", desc=html.escape(a["desc"]), url=url, img=IMG, ogtype="article",
                       ld=ld({"@context": "https://schema.org", "@graph": graph}))
    page += f"""
<main class="wrap article">
  <nav class="crumbs"><a href="/">Acasă</a> › <a href="/blog/">Blog</a> › <span>{a['tag']}</span></nav>
  <span class="eyebrow">{a['tag']}</span>
  <h1>{html.escape(a['title'])}</h1>
  <p class="meta">Echipa Belvedere · {DATE_RO} · {a['read']} min de citit</p>
  <article class="content">
{summary_html}
{a['body']}
    <h2>Întrebări frecvente</h2>
    <div class="faq">{faq_html}</div>
  </article>
  {CTA}
  <section class="related"><h2>Mai citește</h2><div class="rel-grid">{related}</div></section>
</main>
"""
    page += FOOT
    open(os.path.join(ROOT, "blog", a["slug"] + ".html"), "w").write(page)

# index
cards = "\n".join(f"""<a class="card" href="/blog/{a['slug']}.html">
  <span class="eyebrow">{a['tag']} · {a['read']} min</span>
  <h2>{html.escape(a['title'])}</h2>
  <p>{html.escape(a['desc'])}</p>
  <span class="more">Citește articolul →</span>
</a>""" for a in VISIBLE)
idx_ld = ld({"@context": "https://schema.org", "@type": "Blog", "name": "Blogul Belvedere", "url": U + "/blog/", "inLanguage": "ro-RO", "publisher": publisher,
             "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{U}/blog/{a['slug']}.html", "datePublished": DATE} for a in VISIBLE]})
page = HEAD.format(title="Blog Belvedere: ghiduri pentru Târgu Neamț, cazare și gastronomie",
                   desc="Ghiduri și sfaturi pentru Târgu Neamț: ce să vizitezi, Cetatea Neamț, mănăstirile Agapia și Văratec, cazare și preparate moldovenești.",
                   url=U + "/blog/", img=IMG, ogtype="website", ld=idx_ld)
page += f"""
<main class="wrap">
  <section class="blog-hero">
    <span class="eyebrow">Blog</span>
    <h1>Ghiduri pentru Târgu Neamț</h1>
    <p class="lead">Ce să vizitezi, unde să mănânci și cum să-ți organizezi drumul prin Ținutul Neamțului, de la gazdele tale de la Belvedere.</p>
  </section>
  <div class="cards">
{cards}
  </div>
  {CTA}
</main>
"""
page += FOOT
open(os.path.join(ROOT, "blog", "index.html"), "w").write(page)

open(os.path.join(ROOT, "blog", "blog.css"), "w").write(""":root{--ink:#141414;--paper:#faf8f5;--paper-2:#f1ede6;--muted:#6b6660;--line:#e2ddd5;--accent:#e53395;--accent-dark:#c2207b;--radius:14px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.75;font-size:17px}
a{color:var(--accent)}
h1,h2,h3,.brand{font-family:Oswald,Impact,sans-serif;letter-spacing:.03em;text-transform:uppercase;line-height:1.2}
.wrap{max-width:1000px;margin:0 auto;padding:0 20px}
.top{background:var(--ink);position:sticky;top:0;z-index:10}
.nav{display:flex;justify-content:space-between;align-items:center;height:68px;gap:12px}
.brand{color:#fff;text-decoration:none;font-size:1.35rem;font-weight:600;line-height:1}
.brand small{display:block;font-size:.58rem;letter-spacing:.3em;font-weight:400;opacity:.85;margin-top:3px}
.top nav{display:flex;gap:20px;align-items:center}
.top nav a{color:#fff;text-decoration:none;font-size:.92rem;font-weight:500}
.top nav a:hover{color:var(--accent)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:999px;font-weight:600;text-decoration:none;border:2px solid transparent;font-size:.95rem;transition:.2s}
.top nav .btn{padding:8px 16px;color:#fff}
.btn-accent{background:var(--accent);color:#fff}.btn-accent:hover{background:var(--accent-dark)}
.btn-wa{background:#25d366;color:#fff}.btn-wa:hover{background:#1ebe5a}
.btn-outline{border-color:var(--ink);color:var(--ink);background:#fff}.btn-outline:hover{background:var(--ink);color:#fff}
.eyebrow{display:inline-block;color:var(--accent);font-weight:600;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px}
.lead{color:var(--muted);font-size:1.08rem;max-width:640px}
.blog-hero{padding:64px 0 32px}
.blog-hero h1{font-size:clamp(2.2rem,5vw,3.2rem);margin-bottom:12px}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-bottom:48px}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:28px;text-decoration:none;color:var(--ink);display:flex;flex-direction:column;gap:10px;transition:.2s}
.card:hover{border-color:var(--accent);transform:translateY(-2px)}
.card h2{font-size:1.25rem}
.card p{color:var(--muted);font-size:.95rem}
.card .more{color:var(--accent);font-weight:600;font-size:.92rem;margin-top:auto}
.article{max-width:760px;padding-top:36px;padding-bottom:40px}
.crumbs{font-size:.85rem;color:var(--muted);margin-bottom:22px}
.crumbs a{color:var(--muted)}
.article h1{font-size:clamp(1.9rem,4.5vw,2.7rem);margin-bottom:12px}
.meta{color:var(--muted);font-size:.9rem;margin-bottom:28px}
.content .intro{font-size:1.15rem;color:#3a3632;margin-bottom:8px}
.content h2{font-size:1.5rem;margin:40px 0 12px}
.content h3{font-size:1.12rem;margin:26px 0 8px}
.content p{margin-bottom:14px}
.content ul,.content ol{margin:0 0 16px 22px}
.content li{margin-bottom:8px}
.summary{background:#fff3f9;border-left:4px solid var(--accent);border-radius:10px;padding:16px 20px;margin:0 0 22px}
.summary b{display:block;font-family:Oswald,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin-bottom:4px}
.summary p{margin:0;font-size:.98rem}
.faq details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:0 18px;margin-bottom:10px}
.faq summary{cursor:pointer;font-weight:600;padding:14px 0}
.faq details p{color:var(--muted);padding-bottom:14px;margin:0}
.cta{background:var(--ink);color:#fff;border-radius:var(--radius);padding:32px;margin:44px 0}
.cta h3{font-size:1.4rem;margin-bottom:10px}
.cta p{color:#cfc8bf;margin-bottom:20px}
.cta-actions{display:flex;gap:10px;flex-wrap:wrap}
.cta .btn-outline{background:transparent;color:#fff;border-color:#fff}.cta .btn-outline:hover{background:#fff;color:var(--ink)}
.related h2{font-size:1.3rem;margin-bottom:16px}
.rel-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.rel{background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px;text-decoration:none;color:var(--ink);font-weight:600;font-size:.95rem;line-height:1.45}
.rel span{display:block;color:var(--accent);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:6px}
.rel:hover{border-color:var(--accent)}
footer{background:#0d0d0d;color:#8d877f;padding:36px 0;font-size:.88rem;margin-top:40px}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center}
footer .brand{color:#fff;font-size:1.15rem}
footer a{color:#c9c2b8}
@media (max-width:760px){.cards,.rel-grid{grid-template-columns:1fr}.top nav a:not(.btn):not(:first-child){display:none}.cta{padding:24px}}
""")

print("\n".join(a["slug"] for a in ARTICLES))

# ---- sitemap.xml and llms.txt (generated) ----
pages = ["", "politica-confidentialitate.html", "blog/"] + [f"blog/{a['slug']}.html" for a in ARTICLES]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{U}/{p}</loc><lastmod>{DATE}</lastmod></url>\n" for p in pages) + "</urlset>\n")
art_lines = "\n".join(f"- [{a['title']}]({U}/blog/{a['slug']}.html): {a['desc']}" for a in ARTICLES)
open(os.path.join(ROOT, "llms.txt"), "w").write(f"""# Belvedere Gastro Pub & Pensiune

> Restaurant (gastro pub) și pensiune de 3 stele în Târgu Neamț, județul Neamț, România. Adresă: Str. Mărășești nr. 215, 615200 Târgu Neamț. Telefon: +40 747 295 151. Email: rezervari@pensiuneabelvedere.ro.

## Restaurant
- Bucătărie românească și internațională, gastro pub cu bar, cocktailuri, terasă și opțiuni vegane.
- Deschis zilnic, până la ora 22:00.
- Meniul zilei: luni – vineri, 12:00 – 15:00. Joia burgerilor: în fiecare joi.
- Specialitatea casei: șnițelul Belvedere. Recomandate: ciorba dreseală, ciorba de văcuță, coaste de porc, burger gourmet.
- Comenzi și rezervări telefonic: 0747 295 151.

## Pensiune
- Camere duble Deluxe cu balcon și camere twin Deluxe, baie proprie, TV, aparat de cafea/ceai, Wi-Fi gratuit.
- Mic dejun inclus. Parcare privată gratuită. Animale de companie acceptate fără taxe suplimentare.
- Certificare EU Ecolabel. Check-in de la 15:00, check-out până la 12:00.
- Nota 9,1/10 pe Booking.com (peste 530 de evaluări); 96% recomandări pe Facebook.

## Distanțe
- Cetatea Neamț: 3,6 km. Mănăstirea Agapia: 14 km. Mănăstirea Văratec: 15 km. Aeroportul Suceava: 69 km.

## Pagini
- [Pagina principală]({U}/)
- [Blog]({U}/blog/)
{art_lines}
""")
