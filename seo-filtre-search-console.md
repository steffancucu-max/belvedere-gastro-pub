# Filtre regex pentru Google Search Console – Belvedere

Unde le folosești: **Search Console → Performance (Performanță) → + Add filter → Query (Interogare) → Custom (regex)**, apoi lipești filtrul.

Notă: oamenii caută des **fără diacritice** („targu neamt”, „pensiune cu mic dejun”), așa că filtrele de mai jos acceptă ambele variante. `(?i)` face filtrul să ignore literele mari sau mici. În loc de `\b` (granița de cuvânt), filtrele folosesc `(^|\s)` și `(\s|$)`, pentru că `\b` nu funcționează corect cu diacriticele (ă, â, î, ș, ț).

Datele apar în Search Console abia după câteva zile sau săptămâni de la indexare. Până atunci, filtrele nu vor returna nimic.

## 1. Căutări lungi, specifice

| # | Ce găsește | Filtru |
|---|---|---|
| 1 | Căutări de 4+ cuvinte | `^(?:\S+\s+){3,}\S+$` |
| 2 | Căutări foarte specifice (8+ cuvinte) | `^(?:\S+\s+){7,}\S+$` |
| 3 | Căutări detaliate (10+ cuvinte) | `^(?:\S+\s+){9,}\S+$` |
| 4 | Întrebări reale | `(?i)^(cine|ce|care|cum|cand|când|unde|de ce|cat|cât|cate|câte)(\s|$)` |
| 5 | Căutări de tip prompt AI | `(?i)^(recomanda|recomandă|arata|arată|spune|da-mi|dă-mi|lista|listă|ajuta|ajută)(\s|$)` |

## 2. Întrebări și idei de conținut

| # | Ce găsește | Filtru |
|---|---|---|
| 6 | Cum ajung / ghiduri | `(?i)(^|\s)(cum ajung|cum se ajunge|traseu|ghid|ce vizitez|ce sa vizitez|ce să vizitez)(\s|$)` |
| 7 | Program și orar | `(?i)(^|\s)(program|orar|deschis|inchis|închis|ora|ore)(\s|$)` |
| 8 | Întrebări de tip FAQ | `(?i)^(se poate|pot|accepta|acceptă|are|aveti|aveți|este|e)(\s|$)` |
| 9 | Animale, parcare, facilități | `(?i)(^|\s)(animale|caine|câine|pisica|pisică|pet|parcare|wifi|terasa|terasă|gradina|grădină)(\s|$)` |
| 10 | Probleme și reclamații | `(?i)(^|\s)(problema|problemă|reclamatie|reclamație|nu raspunde|nu răspunde|inchis|închis)(\s|$)` |

## 3. Intenție de cumpărare / rezervare

| # | Ce găsește | Filtru |
|---|---|---|
| 11 | Comparații cu concurența | `(?i)(^|\s)(vs|sau|comparatie|comparație|alternativa|alternativă|la cuptor|ladomnizza|taverna|aristocratis|venezia|moldavian)(\s|$)` |
| 12 | Prețuri și tarife | `(?i)(^|\s)(pret|preț|preturi|prețuri|tarif|tarife|cat costa|cât costă|lei|ieftin)(\s|$)` |
| 13 | Recenzii și păreri | `(?i)(^|\s)(recenzii|recenzie|pareri|păreri|review|nota|notă|rating)(\s|$)` |
| 14 | „Cel mai bun” / top | `(?i)(^|\s)(cel mai bun|cea mai buna|cea mai bună|cele mai bune|top|recomandat|bun)(\s|$)` |
| 15 | Rezervări și oferte | `(?i)(^|\s)(rezervare|rezervari|rezervări|rezerva|rezervă|oferta|ofertă|reducere|pachet|booking)(\s|$)` |

## 4. Nișe și oportunități locale

| # | Ce găsește | Filtru |
|---|---|---|
| 16 | Informații noi / sezoniere | `(?i)(^|\s)(nou|noua|nouă|2026|2027|revelion|craciun|crăciun|paste|paște|1 mai|weekend)(\s|$)` |
| 17 | Meniu și preparate | `(?i)(^|\s)(meniu|meniul zilei|snitel|șnițel|ciorba|ciorbă|burger|mic dejun|vegan|pizza)(\s|$)` |
| 18 | Cazare și camere | `(?i)(^|\s)(cazare|pensiune|camera|cameră|camere|hotel|dormit|mic dejun inclus)(\s|$)` |
| 19 | Evenimente | `(?i)(^|\s)(eveniment|nunta|nuntă|botez|aniversare|petrecere|grup|masa festiva|masă festivă)(\s|$)` |
| 20 | Căutări locale / „lângă mine” | `(?i)(^|\s)(langa|lângă|aproape|near me|cetatea|cetate|agapia|varatec|văratec|humulesti|humulești|livrare|comanda|comandă)(\s|$)` |

## Cum le folosești

1. Rulează filtrele o dată pe lună, pe ultimele 3 luni.
2. Uită-te la căutările cu **multe afișări, dar puține clicuri**. Acolo Google te arată, dar oamenii nu intră pe site.
3. Pentru fiecare astfel de căutare, adaugă pe site un răspuns clar: o întrebare în secțiunea „Întrebări frecvente”, un preparat în meniu sau o informație despre cazare.
