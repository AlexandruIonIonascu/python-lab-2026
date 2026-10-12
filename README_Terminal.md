# Terminalul: unde dai comenzi și vezi rezultatele

Terminalul este interfața text. În el rulează un **shell** (în acest laborator Bash),
care citește comenzile și pornește programe precum Python sau Git.
Editorul modifică fișiere; terminalul execută comenzi. Terminalul nu este un fișier Python.

Deschide **Terminal → New Terminal** în Codespaces. Linia care așteaptă o comandă
se numește prompt. Nu copia semnele `$` sau `>>>` din exemple de pe internet.
În ghidurile noastre comenzile se copiază fără astfel de semne.

| Comandă | Ce face | Ce observi |
| --- | --- | --- |
| `pwd` | Arată directorul curent | O cale precum `/workspaces/python-lab-2026-COD` |
| `ls` | Listează fișierele vizibile | `app.py`, ghiduri, foldere |
| `ls -a` | Include numele care încep cu punct | `.git`, `.gitignore`, `.devcontainer` |
| `cd dovezi` | Intră în folder | Următorul `pwd` se schimbă |
| `cd ..` | Revine în folderul părinte | Ești iar în rădăcina proiectului |
| `mkdir -p dovezi` | Creează folderul dacă lipsește | Nu afișează neapărat un mesaj |
| `cat app.py` | Afișează sursa ca text | Nu execută Python |
| `python --version` | Cere versiunea interpretorului | În mediul configurat: Python 3.12.x |
| `python app.py` | Execută fișierul prin Python | Mesajele produse de program |
| `git status` | Arată starea Git | Modificări și relația cu branch-ul remote |

## Shell sau Python?

În shell scrii `python app.py`, `pwd` sau `git status`.
În `app.py` scrii `print("Salut!")`. `print` este o funcție Python;
`print("Salut!")` scris direct în Bash poate da eroare de sintaxă.

Comanda `python` fără numele fișierului deschide interpretorul interactiv (REPL).
La promptul `>>>` poți scrie expresii Python, dar `git status` nu este Python.
Scrie `exit()` pentru a reveni în shell. `Ctrl+C` întrerupe un program care rulează;
pentru o aplicație care așteaptă `input`, introdu răspunsul sau întrerupe cu `Ctrl+C`.

## Redirecționarea output-ului

Din rădăcina repository-ului:

```bash
python app.py > dovezi/output_lab1.txt
cat dovezi/output_lab1.txt
```

`>` este interpretat de shell și scrie output-ul standard în fișier. Suprascrie
fișierul dacă există. Programul a rulat chiar dacă mesajele nu au apărut pe ecran.
Fișierul nu ajunge pe GitHub până nu îl adaugi, faci commit și push.
Erorile pot apărea în continuare în terminal, fiind scrise pe fluxul de erori.

## Exercițiul de navigare

Rulează `pwd`, `ls`, `ls -a`, `cd dovezi`, `pwd`, `cd ..` și `pwd`.
Completează jurnalul cu ce s-a schimbat. Creează un fișier din shell:

```bash
printf 'Am creat acest fisier din terminal.\n' > dovezi/terminal.txt
cat dovezi/terminal.txt
git status --short
```

`printf` este aici o comandă a shell-ului; nu este funcția Python `print`.
Observă fișierul și în Explorer. Nu folosi comenzi de ștergere recursive în acest laborator.
