# Depanare rapidă

| Simptom | Verificare și remediu |
| --- | --- |
| Nu apare Use this template | Profesorul trebuie să activeze Settings → Template repository; verifică și accesul la template |
| Remote-ul este repository-ul profesorului | Oprește lucrul acolo; creează copia cu Use this template și deschide Codespaces din copia ta |
| `python: command not found` | Verifică terminalul Codespaces și finalizarea configurării; încearcă `python3 --version`; în mediul local poți avea nevoie de `python3` sau `py` |
| Nu apare Python: Select Interpreter | Verifică extensia Microsoft Python instalată și activă în Codespace; reîncarcă editorul |
| `can't open file ... app.py` | `pwd`, `ls`; revino în rădăcina repository-ului sau folosește calea corectă |
| Văd codul în loc de mesaje | `cat app.py` citește sursa; `python app.py` o execută |
| Output-ul nu se schimbă | Save All, verifică fișierul și calea, rerulează; mesajele vechi rămân în terminal |
| `>>>` și comenzile Git dau erori | Ești în Python REPL; `exit()` și rulează Git în shell |
| Programul pare blocat | Poate așteaptă `input`; tastează răspunsul și Enter sau oprește cu Ctrl+C |
| `ValueError` la preț | Introdu `12.5`, nu `12,5`; datele de bază trebuie să fie valide |
| `nothing to commit` | Verifică Save, `git status` și fișierele adăugate; poate schimbarea a fost deja committed |
| `Author identity unknown` | Configurează `git config user.name "Numele tau"` și `git config user.email "EMAIL_GITHUB"` cu datele tale; poți folosi adresa noreply din GitHub Settings → Emails |
| Push 403 / Permission denied | Verifică remote-ul și contul; ai nevoie de drept de scriere în propria copie. Nu introduce un token în fișier sau chat |
| Push rejected / non-fast-forward | Există schimbări remote; salvează și fă commit local, apoi `git pull --rebase origin main`. Dacă apar conflicte, cere ajutor profesorului. Nu folosi force push |
| Conflict la rebase | Profesorul te ajută să inspectezi `git status` și markerii; dacă vrei să revii la starea de dinaintea rebase-ului folosește `git rebase --abort` |
| Working tree curat, dar profesorul nu vede codul | Verifică push, branch, remote, SHA în browser și accesul profesorului |
| Profesorul primește 404 la un repo privat | Verifică username-ul invitației și acceptarea ei; trimite URL-ul repository-ului, nu al Codespace-ului |
| Copilot nu sugerează | Verifică autentificarea, extensia, activarea sugestiilor pentru Python, planul și limitele; folosește varianta din README_Copilot.md |
| Codespaces nu pornește / cotă epuizată | Verifică mesajul exact și billing-ul; nu cumpăra resurse. Anunță profesorul și folosește varianta locală |

## Variantă locală pentru lipsă de Codespaces

Profesorul te ajută să instalezi Git, Python 3.12 sau mai nou, VS Code și extensia
Microsoft Python. Clonează **repository-ul tău creat din template** prin Source
Control → Clone Repository în VS Code și autentifică-te cu contul tău GitHub.
Deschide folderul clonat, selectează interpretorul și rulează din terminal.

Pe macOS/Linux poate fi nevoie de `python3`; pe Windows de `py`. Pentru comenzile
de shell din acest ghid folosește Bash (Git Bash pe Windows), sau creează fișierul
`dovezi/terminal.txt` cu o comandă echivalentă demonstrată de profesor. Notează mediul
folosit și diferențele în jurnal. Save / add / commit / push și verificarea în browser
rămân necesare. Editorul `github.dev` singur nu înlocuiește mediul de execuție local.
