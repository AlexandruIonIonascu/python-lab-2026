# Primele aplicații Python: GitHub, terminal, Codespaces și Copilot

**Două laboratoare de 90 de minute • lucru individual • ediția 2026**

La final poți crea și rula o aplicație Python, explica rezultatul din terminal,
corecta erori, folosi critic Copilot și preda codul pe GitHub prin commit și push.
Nu ai nevoie de experiență anterioară. Citește instrucțiunile pe rând, în timpul lucrului.

## Înainte de laborator

1. Creează un cont GitHub și verifică adresa de e-mail. Reține username-ul.
2. Profesorul îți comunică linkul template-ului, username-ul său, codul tău de student,
   locul predării (LMS/formular) și cele două termene. Nu ghici aceste informații.
3. Poți solicita beneficiile [GitHub Education](https://github.com/settings/education/benefits)
   din timp. Aprobarea nu este o condiție pentru începerea laboratorului.
4. Ai nevoie de browser și internet. În Codespaces, Python rulează pe calculatorul
   din cloud; nu trebuie instalat pe laptop. Extensia Python din editor este un lucru separat.

## Creează copia ta, apoi deschide Codespaces

1. Deschide template-ul transmis de profesor → **Use this template → Create a new repository**.
   Nu alege „Open in a codespace” direct din template.
2. Owner: contul tău. Nume: `python-lab-2026-COD`, înlocuind `COD` cu identificatorul
   comunicat de profesor. Alege **Private**. Nu bifa „Include all branches”.
3. În repository-ul tău: **Settings → Collaborators** (denumirea poate varia)
   → **Add people** → username-ul exact al profesorului → invitație.
   Profesorul trebuie să accepte invitația pentru a citi un repository privat.
4. Tot în repository-ul tău: **Code → Codespaces → Create codespace on main**.
   Alege 2 cores dacă ai opțiunea. Prima pornire poate dura câteva minute.
5. Așteaptă finalizarea configurării. Urmează [ghidul Codespaces](README_Codespaces.md)
   pentru instalarea/verificarea extensiei Python și alegerea interpretorului.
6. În terminalul Codespaces rulează `git remote -v`. Adresa trebuie să conțină
   username-ul tău și repository-ul tău, nu repository-ul profesorului.

**Nu lucra în template-ul profesorului. Nu trimite un pull request către template.**
Fiecare student predă propriul repository; ambele laboratoare se fac în aceeași copie.

## Ordinea de lucru

| Când | Material | Rezultatul pe care îl predai |
| --- | --- | --- |
| Laboratorul 1 | [LAB_01.md](LAB_01.md) | `app.py`, jurnal, fișier creat din terminal, cel puțin 2 commit-uri proprii |
| Laboratorul 2 | [LAB_02.md](LAB_02.md) | miniaplicație, depanare, jurnal Copilot, cel puțin încă 2 commit-uri proprii |
| După fiecare sesiune | [PREDARE.md](PREDARE.md) | URL repository + link commit + acces confirmat pentru profesor |

## Harta fișierelor

| Fișier / folder | Rol | Îl modifici? |
| --- | --- | --- |
| `README.md` | Punctul de pornire | Nu este necesar |
| `LAB_01.md`, `LAB_02.md` | Cerințe și pași | Nu |
| `README_GitHub.md` | Git, repository, commit, push | Nu |
| `README_PY.md` | Python, `print`, `input`, erori | Nu |
| `README_Terminal.md` | Comenzi și navigare | Nu |
| `README_Codespaces.md` | Mediul cloud și extensiile | Nu |
| `README_Copilot.md` | AI folosit cu explicație și verificare | Nu |
| `app.py` | Prima aplicație | Da, laboratorul 1 |
| `miniapp.py` | Calculator de cost | Da, laboratorul 2 |
| `exercitii/*.py` | Trei programe cu erori intenționate | Da, laboratorul 2 |
| `raspunsuri/*.md` | Dovezi și explicații proprii | Da |
| `dovezi/` | Rezultate de rulare și fișierul creat în terminal | Da |
| `tools/verifica.py` | Verificare locală a unor cerințe | Nu |
| `.devcontainer/devcontainer.json` | Python 3.12 și editorul în Codespaces | Nu |
| `.github/workflows/verificare.yml` | Verificare manuală din GitHub Actions | Nu |
| `.github/copilot-instructions.md` | Instrucțiuni orientative pentru Copilot | Nu |
| `.gitignore` | Fișiere pe care Git le ignoră | Doar exercițiul explicativ |
| `LICENSE` | Licența materialului | Nu |

Folderele organizează proiectul. `exercitii/nume.py` este o cale relativă față de
rădăcina repository-ului. Literele mari/mici contează în Linux: `README_PY.md` este
alt nume decât `README_Python.md`. Git păstrează fișiere, nu foldere goale.
Folderul intern `.git/` conține istoricul local; nu îl modifica și nu îl șterge.

## Cele patru operații distincte

**Save** scrie fișierul în Codespaces. **Run** execută programul și produce output.
**Commit** înregistrează o versiune în istoricul Git din Codespaces.
**Push** trimite commit-ul pe GitHub, unde profesorul îl poate vedea dacă are acces.
Nici rularea, nici un commit fără push nu reprezintă predare completă.

## Ajutor rapid

Pentru probleme consultă [DEPANARE.md](DEPANARE.md). Dacă nu poți crea un Codespace,
anunță profesorul; există varianta locală descrisă acolo. Nu cumpăra un abonament
pentru laborator. Sursele oficiale și data verificării sunt în [SURSE.md](SURSE.md).
