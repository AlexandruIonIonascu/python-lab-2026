# Laboratorul 1 — scriu, rulez, explic și predau (90 minute)

Lucrezi fără Copilot și fără alte generatoare AI. Profesorul te poate ajuta cu
instalarea și comenzile, dar predicțiile și explicațiile îți aparțin.
Ține deschis `raspunsuri/lab1.md` și completează-l în timpul exercițiilor.

| Minute | Activitate | Checkpoint |
| --- | --- | --- |
| 0–8 | Diferența GitHub / Codespace / editor / terminal | Identifici cele patru componente |
| 8–23 | Copie privată, acces profesor, Codespace, extensia Python | Remote corect și Python funcțional |
| 23–35 | Navigare și fișier creat în terminal | `dovezi/terminal.txt` |
| 35–48 | Primul program și primul commit + push | Commit 1 vizibil în browser |
| 48–70 | Experimente `print`: prezic → rulez → explic | Program și tabel de observații |
| 70–80 | `.gitignore`, output într-un fișier, verificare locală | Dovezi și jurnal complet |
| 80–90 | Al doilea commit + push + predare | SHA pe GitHub și acces profesor |

## 1. Pregătirea mediului

Urmează README.md și README_Codespaces.md. Instalează/verifică extensia Microsoft
Python și selectează interpretorul. În terminal, din rădăcina proiectului:

```bash
pwd
ls
ls -a
python --version
git --version
git remote -v
git branch --show-current
```

Notează versiunile, branch-ul (`main`), remote-ul și rolul a patru fișiere/foldere.
Nu copia toate logurile de pornire. Arată profesorului extensia activă și interpretorul.

## 2. Terminal și fișiere

Urmează exercițiul de navigare din README_Terminal.md și creează
`dovezi/terminal.txt` cu `printf`. Scrie în jurnal calea înainte și după `cd dovezi`
și de ce `python app.py` din acel folder nu găsește fișierul.
Revino cu `cd ..` înainte de comenzile următoare.

## 3. Prima rulare și checkpoint-ul 1

1. Citește `app.py`. Prezice output-ul și rulează `python app.py`.
2. Adaugă o variabilă `alias` cu prenumele sau un pseudonim și un apel `print`
   care produce `Salut, ALIAS!`, folosind valoarea variabilei. Nu pune date sensibile.
3. Salvează și rulează atât din terminal, cât și prin **Run Python File in Terminal**.
4. Completează secțiunile „Mediu”, „Navigare” și „Prima rulare” din jurnal.
5. Creează primul commit propriu:

```bash
git status
git diff
git add app.py raspunsuri/lab1.md dovezi/terminal.txt
git diff --staged
git commit -m "Configureaza mediul si adauga salutul personal"
git push origin main
```

Deschide copia ta pe GitHub și verifică noul salut. Notează SHA-ul commit-ului
în jurnal după commit; informația va intra în următorul commit.
Profesorul verifică dacă poate deschide repository-ul privat.

## 4. Experimente `print`

Pentru fiecare experiment: **scrie predicția în jurnal înainte de rulare**, rulează,
apoi notează rezultatul și explicația. Construiește `app.py` progresiv, fără input.
Păstrează salutul inițial și salutul personal ca primele două linii ale output-ului.

| Experiment | Sarcină | Ce explici în jurnal |
| --- | --- | --- |
| P1 | Afișează `GIT|PYTHON|TERMINAL` printr-un singur `print` cu 3 argumente și `sep` | Separatorul și lipsa spațiilor |
| P2 | Cu două apeluri `print`, afișează `Pornesc...gata!` pe aceeași linie | `end` la primul apel |
| P3 | Adaugă un apel `print()` fără argumente | De ce apare o linie goală |
| P4 | Afișează rezultatul lui `2 + 3`, apoi al lui `"2" + "3"` | Numere față de text |
| P5 | Afișează `Linia 1` și `Linia 2` cu un singur `print` și `\n` | Rând nou în interiorul șirului |
| P6 | Afișează `Mesaj personal: ` urmat de un mesaj ales de tine | Ghilimelele și textul propriu |

Output-ul final trebuie să aibă **10 linii**, în această ordine (linia 5 este goală):

```text
Hello, world!
Salut, ALIAS!
GIT|PYTHON|TERMINAL
Pornesc...gata!

5
23
Linia 1
Linia 2
Mesaj personal: MESAJUL TAU
```

Înlocuiești `ALIAS` și `MESAJUL TAU`. Folosește efectiv `sep`, `end`, `print()` și
operațiile cerute; simpla scriere a unui șir mare cu rezultatul nu îndeplinește sarcina.
Adaugă cel puțin două comentarii care explică deciziile tale.

## 5. Git ignore și output

Din rădăcina proiectului:

```bash
printf 'Exercitiu local, nu se preda.\n' > experiment.local.txt
git status --short
git check-ignore -v experiment.local.txt
python app.py > dovezi/output_lab1.txt
cat dovezi/output_lab1.txt
python tools/verifica.py lab1
```

Explică de ce `experiment.local.txt` nu apare ca fișier nou de predate și ce regulă
din `.gitignore` îl exclude. Compară `cat app.py` cu `python app.py`: sursă față de
output. Nu modifica verificatorul pentru a trece verificarea.

## 6. Checkpoint-ul 2 și predarea

Completează jurnalul și răspunde fără AI: ce ar putea vedea profesorul dacă ai
făcut doar Save? Dar numai commit? Ce se schimbă după push?

```bash
git add app.py raspunsuri/lab1.md dovezi/output_lab1.txt
git diff --staged
git commit -m "Completeaza experimentele print si dovezile lab1"
git push origin main
git status
git log --oneline -5
git rev-parse HEAD
```

Urmează PREDARE.md. Ai nevoie de cel puțin **2 commit-uri proprii cu schimbări reale**,
în plus față de commit-ul inițial al template-ului. Nu folosi commit-uri goale.
Oprește Codespace-ul după ce ai verificat predarea în browser.

## Verificare individuală, fără notițe (2 minute)

Profesorul îți cere să schimbi separatorul din P1 din `|` în ` / `, să prezici
output-ul, să rulezi și să explici unde faci push. Revino la forma cerută, salvează
și rulează din nou. Dacă faci o schimbare permanentă, include-o într-un nou commit.
