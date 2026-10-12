# Codespaces și extensia Python

Un Codespace este un mediu de dezvoltare găzduit în cloud. În browser vezi editorul
VS Code; fișierele, terminalul, Git și interpretorul rulează în mediul Linux din cloud.
Nu confunda Codespaces cu `github.dev`: acesta din urmă este un editor web și nu
oferă același mediu de execuție cu terminal și interpretor.

## Ce asigură acest proiect

`.devcontainer/devcontainer.json` folosește imaginea oficială devcontainers pentru
Python 3.12. Nu sunt necesare biblioteci instalate cu pip. La pornire se verifică
versiunile Python și Git. Extensiile nu sunt instalate automat în configurația de
bază: instalarea extensiei Python este un exercițiu explicit și verificabil.

## Instalarea extensiei Python în Codespace

1. În editorul Codespaces deschide **Extensions** din bara laterală.
2. Caută **Python**, publisher **Microsoft**, identificator `ms-python.python`.
3. Dacă lipsește, apasă **Install** pentru mediul Codespaces. Dacă este deja instalată
   (de exemplu prin Settings Sync), verifică să fie activată în Codespace și notează
   „deja instalată” în jurnal. Nu trebuie reinstalată inutil.
4. Deschide `app.py`. Din Command Palette (`F1` sau `Ctrl+Shift+P`) selectează
   **Python: Select Interpreter** → interpretorul Python 3.12 din container.
5. Rulează în terminal `python --version`. Notează și interpretorul selectat în editor.
6. Folosește **Run Python File in Terminal** pentru `app.py`. Compară cu rezultatul
   comenzii `python app.py` din shell. Trebuie să vezi același output.

Extensia oferă ajutor de editare, rulare și depanare; **nu conține interpretorul**.
Interpretorul este deja în imaginea acestui Codespace. Dacă dezactivezi extensia,
`python app.py` funcționează în continuare, atât timp cât Python este instalat.

## Cele trei zone pe care le identifici

Explorer: fișierele și folderele. Editor: conținutul fișierului selectat.
Terminal: comenzile și output-ul. Source Control: modificările și commit-urile.
În jurnal explică unde ai scris codul și unde l-ai executat.

## Încheiere și reluare

După push și verificare pe GitHub: `F1` → **Codespaces: Stop Current Codespace**,
sau [github.com/codespaces](https://github.com/codespaces) → meniul Codespace-ului → Stop.
Simpla închidere a tabului nu garantează oprirea imediată. La laboratorul 2 redeschide
același Codespace; nu crea unul nou fără motiv. Stop păstrează mediul și fișierele.
Ștergerea Codespace-ului poate pierde fișiere și commit-uri care nu au fost pushed.

## Utilizare inclusă și costuri

La verificarea din 12 octombrie 2026, contul personal Free include 120 core-hours
și 15 GB de stocare pe lună; Pro include 180 core-hours și 20 GB. Core-hours nu sunt
ore de ceas: 90 de minute pe 2 cores consumă aproximativ 3 core-hours; două sesiuni
aproximativ 6, plus timpul în care mediul mai rulează. Stocarea se contorizează și
când Codespace-ul este oprit. Verifică valorile actuale în pagina de billing a contului.
Nu porni trial-uri sau consum plătit pentru acest assignment. Dacă nu ai cotă,
anunță profesorul și folosește varianta locală din DEPANARE.md.
