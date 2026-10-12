# Laboratorul 2 — depanez, construiesc și verific Copilot (90 minute)

Redeschide același Codespace și aceeași copie. Primele două etape sunt fără AI.

| Minute | Activitate | Checkpoint |
| --- | --- | --- |
| 0–10 | Recapitulare individuală și verificare predare L1 | Explici Save / Run / Commit / Push |
| 10–27 | Trei erori, înainte și după corectare | Jurnal de depanare |
| 27–35 | Commit + push de depanare | Commit 3 vizibil pe GitHub |
| 35–47 | Introducere `input`, conversii și cerința miniaplicației | Prezici trei rezultate |
| 47–67 | Copilot: explicație, propunere limitată și critică | Jurnal cu decizii și verificări |
| 67–80 | Implementare și trei teste | Output corect și dovezi |
| 80–90 | Explicație orală, commit + push și predare finală | Commit 4 și acces verificat |

## 1. Recapitulare

Din rădăcina proiectului rulează `git status`, `git remote -v`, `python app.py` și
`python tools/verifica.py lab1`. Verifică în browser commit-ul predat la L1.
Spune în cuvintele tale de ce nu este suficient să închizi tabul după Save.
Dacă ai lucrat și din alt mediu, sincronizează numai după indicațiile din DEPANARE.md.

## 2. Depanare fără Copilot

Rulează separat:

```bash
python exercitii/eroare_sintaxa.py
python exercitii/eroare_nume.py
python exercitii/eroare_tip.py
```

Pentru fiecare fișier completează `raspunsuri/lab2.md`: ce ai prezis, ultima linie
a mesajului de eroare, linia indicată, cauza, modificarea minimă și output-ul de după.
Corectează fișierele astfel încât să afișeze exact, în ordine: `Incep depanarea`,
`Invat Python`, respectiv `Total: 5`. Nu șterge fișierele și nu comenta întregul program.
Verifică prin rerulare; un mesaj dispărut din editor nu dovedește corectitudinea.

```bash
git add exercitii/eroare_sintaxa.py exercitii/eroare_nume.py exercitii/eroare_tip.py raspunsuri/lab2.md
git diff --staged
git commit -m "Corecteaza trei erori si explica depanarea"
git push origin main
```

Notează SHA-ul în jurnal după commit. Îl incluzi în următorul commit.

## 3. Cerința miniaplicației: calculatorul de cost

În `miniapp.py` construiești o aplicație de terminal care:

1. Citește un alias cu `input` și îl afișează în forma `Salut, ALIAS!`.
2. Citește cantitatea, un întreg nenegativ, și prețul unitar, un număr nenegativ.
   Pentru zecimale utilizatorul folosește punctul: `12.5`, nu `12,5`.
3. Transformă input-urile numerice cu `int` și `float`.
4. Calculează `total = cantitate * pret_unitar` folosind variabilele citite.
5. Afișează o linie `Total: XX.XX`, fără monedă sau alte sufixe, cu două zecimale.
6. Conține cel puțin două comentarii utile. Nu folosește pachete externe.

Prompturile de input pot avea textul ales de tine, dar fiecare se termină cu `\n`,
de exemplu `input("Alias:\n")`. Astfel și output-ul unei rulări automate este ușor
de citit, iar `Salut, ...!` și `Total: ...` sunt linii distincte.
Poți folosi un prompt obișnuit fără `\n` în experimente; pentru forma predată aplică
cerința de mai sus. Nu afișa în plus alte linii care încep cu `Salut, ` sau `Total: `.

### Trei teste obligatorii

Înainte de rulare completează predicțiile din jurnal. Rulează `python miniapp.py`
de trei ori și introdu datele de mai jos, fiecare pe câte o linie:

| Caz | Alias | Cantitate | Preț unitar | Linia finală așteptată |
| --- | --- | --- | --- | --- |
| T1 | Ada | 2 | 12.5 | `Total: 25.00` |
| T2 | Lin | 0 | 9.99 | `Total: 0.00` |
| T3 | Sam | 3 | 0.1 | `Total: 0.30` |

Explică de ce T2 testează un caz-limită și de ce T3 testează afișarea zecimalelor.
Nu scrie rezultate fixe pentru aceste trei cazuri: aplicația trebuie să calculeze
corect și alte cantități/prețuri valide. Profesorul testează un caz nou.

## 4. Copilot cu dovezi

Activează Copilot și urmează sarcinile A, B, C din README_Copilot.md.
Completează `raspunsuri/copilot.md` în timpul folosirii, nu inventa ulterior prompturi.
Poți construi scheletul singur și cere numai ajutorul limitat prevăzut în sarcina B.
Cel puțin o propunere trebuie adaptată/refuzată cu o explicație concretă.
Pentru lipsă de acces urmează varianta de demonstrație și recuperare din ghid.

## 5. Verificare și dovezi

Salvează tot, apoi rulează:

```bash
python tools/verifica.py lab2
python tools/verifica.py toate
```

Verificatorul execută aplicațiile cu timeout și compară unele rezultate. Nu evaluează
calitatea explicațiilor, folosirea reală a Copilot sau dovada push-ului.
Un rezultat PASS nu este nota finală. Cerințele de implementare sunt verificate și manual.
În template, verificările eșuează intenționat până completezi exercițiile.

Pentru o dovadă care poate fi citită în repository:

```bash
printf 'Ada\n2\n12.5\n' | python miniapp.py > dovezi/output_lab2.txt
cat dovezi/output_lab2.txt
```

Comanda `|` trimite output-ul `printf` la input-ul programului Python. Notează
în jurnal și rezultatele T2 și T3 obținute în rulările interactive.

## 6. Predare finală

```bash
git add miniapp.py exercitii/eroare_sintaxa.py exercitii/eroare_nume.py exercitii/eroare_tip.py raspunsuri/lab2.md raspunsuri/copilot.md dovezi/output_lab2.txt
git diff --staged
git commit -m "Adauga calculatorul de cost si verifica sugestiile Copilot"
git push origin main
git status
git log --oneline -6
git rev-parse HEAD
```

Urmează PREDARE.md. La final ai minimum **4 commit-uri proprii** cu schimbări reale:
două din L1 și încă două din L2. Nu se numără commit-ul inițial al template-ului.
Oprește Codespace-ul după verificarea în browser.

## Verificare individuală fără AI (2 minute)

Profesorul alege un alias, o cantitate și un preț noi. Prezici totalul, rulezi,
explici tipul valorilor returnate de `input` și de ce conversia este necesară.
Arăți unde se află commit-ul final și o propunere Copilot pe care ai adaptat-o.

## Extensii opționale, după cerințele de bază

- Validează input-ul cu `try/except ValueError` și respinge valori negative; explică
  blocurile noi și testează input valid, invalid și negativ. Păstrează output-ul de bază.
- Creează branch-ul `imbunatatire-mesaje`, adaugă o explicație într-un comentariu,
  fă commit, `git push -u origin imbunatatire-mesaje`, apoi deschide un pull request
  **în repository-ul tău** către `main`. După merge, revino în `main` și sincronizează.
  Predarea de bază trebuie să rămână pe `main`.
