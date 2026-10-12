# Predarea: codul este pe GitHub și profesorul are acces

Predarea este individuală. Profesorul comunică înainte de laborator username-ul
GitHub, codul de repository, canalul de predare și termenele pentru L1 și L2.
În lipsa acestor informații cere-le; nu trimite linkul într-un issue public.

## La sfârșitul fiecărui laborator

1. Salvează și rulează aplicația. Rulează verificatorul pentru etapa curentă.
2. Fă `git add`, commit și **push** pentru toate fișierele cerute.
3. Confirmă `main`, remote-ul și starea cu `git status` și `git remote -v`.
4. Rulează `git rev-parse HEAD` și copiază SHA-ul complet al commit-ului predat.
5. Deschide repository-ul tău în browser, pe `main`, și deschide ultimul commit.
   SHA-ul din browser trebuie să corespundă celui din terminal. Citește acolo codul
   și jurnalul; nu trimite linkul Codespace-ului.
6. Verifică invitația profesorului la repository-ul privat. „Pending” nu înseamnă
   acces acordat: profesorul trebuie să accepte și să confirme că îl poate deschide.
7. În LMS/formularul comunicat predai:

```text
Cod student / grupa:
Username GitHub:
Etapa: L1 / L2
Repository: https://github.com/USERNAME/python-lab-2026-COD
Commit: https://github.com/USERNAME/python-lab-2026-COD/commit/SHA_COMPLET
SHA complet:
Verificare locală: PASS / problema întâmpinată
Acces profesor: confirmat / invitație în așteptare
Copilot (la L2): folosit individual / demonstrație observată, recuperare necesară
```

Completează valorile, nu preda acest șablon. Dacă nu ai PASS, predă progresul și
eroarea exactă la termen; profesorul stabilește recuperarea. Nu declara accesul
„confirmat” până când profesorul nu a putut deschide repository-ul.

## Ce fișiere trebuie să existe

**L1:** `app.py`, `raspunsuri/lab1.md`, `dovezi/terminal.txt`, `dovezi/output_lab1.txt`.

**L2:** toate cele de la L1, plus `miniapp.py`, cele trei fișiere din `exercitii/`,
`raspunsuri/lab2.md`, `raspunsuri/copilot.md`, `dovezi/output_lab2.txt`.
Păstrează ghidurile și configurația. Nu preda doar capturi de ecran sau un ZIP;
profesorul trebuie să poată citi codul și istoricul în repository.

## După predare

Commit-ul trimis în formular este versiunea evaluată. Poți continua să lucrezi,
dar pentru o nouă predare trimite noul link de commit conform regulii profesorului.
Nu încerca să adaugi SHA-ul commit-ului final în același commit: identificatorul
se obține după crearea commit-ului și se trimite separat în LMS/formular.
