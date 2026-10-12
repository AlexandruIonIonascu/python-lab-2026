# Git, GitHub și predarea codului

**Git** urmărește versiunile proiectului. **GitHub** găzduiește repository-ul remote
și permite citirea codului și a istoricului. **Codespaces** este mediul de lucru
din cloud cu o copie a repository-ului și un istoric Git local.
„Local” în comenzile Git înseamnă aici în Codespaces, nu pe laptopul tău.

## Ce înseamnă o modificare

| Stare | Unde este modificarea? | O vede profesorul pe GitHub? |
| --- | --- | --- |
| Ai tastat, fără Save | În editor | Nu |
| Ai salvat fișierul | În copia din Codespaces | Nu |
| Ai folosit `git add` | În staging: selecția pentru următorul commit | Nu |
| Ai făcut commit | În istoricul Git din Codespaces | Nu, încă |
| Ai făcut push | Și în repository-ul GitHub | Da, dacă are acces |

`main` este branch-ul folosit pentru predare. `origin` este numele convențional
al repository-ului remote. `origin/main` reprezintă starea remote cunoscută de Git.
Un commit are un identificator SHA și un mesaj. Mesajul explică schimbarea:
`Completeaza experimentele print` este mai util decât `update`.

## Ciclu de lucru în terminal

1. Salvează fișierele: **File → Save All** sau `Ctrl+S` pentru fișierul curent.
2. Din rădăcina proiectului inspectează:

```bash
git status
git diff
```

3. Selectează fișierele cerute; exemplu pentru primul checkpoint:

```bash
git add app.py raspunsuri/lab1.md dovezi/terminal.txt
git diff --staged
git commit -m "Configureaza mediul si adauga salutul personal"
git push origin main
```

Folosește comanda de `git add` potrivită checkpoint-ului. La ultimul checkpoint
din laboratorul 1 adaugi și `dovezi/output_lab1.txt`. `git diff --staged` arată ce
va intra în commit. Fișierele noi apar întâi ca „untracked”; în `git status --short`,
`??` indică un fișier neadăugat, ` M` o modificare neselectată, `M ` una în staging.
`git diff` arată schimbările neadăugate din fișiere urmărite, nu conținutul tuturor
fișierelor noi.

4. Verifică:

```bash
git status
git log --oneline -5
git rev-parse HEAD
git remote -v
```

Un working tree curat **nu dovedește singur push-ul**. Poți avea commit-uri locale
care nu au ajuns pe GitHub. Deschide repository-ul în browser și confirmă SHA-ul
ultimului commit, apoi deschide `app.py` și citește modificarea.

## Varianta cu interfața Source Control

În Codespaces, deschide Source Control, inspectează diff-ul, apasă `+` la fișierele
cerute (stage), scrie mesajul, apoi **Commit** și **Push / Sync Changes**.
Sync poate face și pull, și push. În acest laborator folosești terminalul cel puțin
o dată pentru fiecare operație, ca să poți explica ce s-a întâmplat.

## Template, fork și pull request

Din template creezi un repository independent cu fișierele de pornire și un
istoric nou. Un fork păstrează legătura și istoricul proiectului părinte.
Pentru acest assignment folosim **Use this template**, nu Fork.
Actualizările template-ului nu se propagă automat în copiile studenților.
Un pull request propune integrarea unui branch în alt branch; nu este necesar
pentru predarea de bază. În laboratorul 2 există o variantă opțională în copia ta.

## `.gitignore`

Acest fișier îi spune lui Git ce fișiere noi să ignore, de exemplu `.venv/`,
`__pycache__/`, `.env` și `*.local.txt`. Nu ascunde automat un fișier deja urmărit.
Fișierele din `dovezi/` trebuie predate și nu sunt ignorate. Nu încărca parole,
tokenuri, documente de identitate sau datele colegilor în repository.
