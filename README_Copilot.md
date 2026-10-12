# Copilot: propune, dar tu verifici și explici

GitHub Copilot este un asistent AI pentru programare. Poate sugera cod în editor,
explica un fragment în chat și ajuta la investigarea unei erori. Sugestiile pot
conține greșeli sau pot încălca cerința. Un rezultat generat nu dovedește înțelegere.

## Activare în Codespaces

1. Verifică planul în [setările Copilot](https://github.com/settings/copilot).
   Copilot Student este destinat studenților verificați prin GitHub Education;
   beneficiul trebuie activat după verificare. Dacă nu este disponibil încă,
   folosește Copilot Free dacă este disponibil pentru contul tău.
2. În editor caută **GitHub Copilot**, publisher **GitHub**, în Extensions sau
   folosește acțiunea de configurare Copilot din bara de stare. Urmează autentificarea
   cu același cont GitHub. Verifică și funcția Chat; editorul poate gestiona separat
   componentele Copilot / Copilot Chat, în funcție de versiune.
3. În chat alege modul de întrebări (**Ask**, dacă apare). Pentru acest laborator
   nu delega întregul assignment în Agent și nu permite executarea automată a comenzilor.
4. Pentru completări, textul sugerat apare de obicei estompat. Citește-l înainte de
   acceptare; `Tab` acceptă de regulă sugestia, `Esc` o respinge. Tastele pot varia.

Planurile gratuite au limite. Student nu înseamnă acces nelimitat la toate modelele;
în documentația actuală Free și Student folosesc selecția automată a modelului.
Nu este necesar să cumperi Copilot Pro. Nu alegem un model anume pentru exerciții.

## Regulile laboratorului

- Laboratorul 1 și prima corectare a erorilor din laboratorul 2 se fac fără AI.
  Dezactivează sugestiile Copilot pentru Python din meniul Copilot dacă apar.
- După checkpoint-ul de depanare activezi Copilot și păstrezi un jurnal al folosirii.
- Nu introduci în prompt parole, tokenuri, date personale sau cod privat al altora.
- Nu accepți comenzi pe care nu le poți explica. `git diff` îți arată ce s-a schimbat.
- `.github/copilot-instructions.md` cere indicii și explicații; aceste instrucțiuni
  sunt orientative, nu împiedică tehnic generarea soluției.

## Trei sarcini cu dovezi

**A. Explicație.** Selectează un fragment cu `print`, `sep` și `end` din `app.py`.
Prompt: „Explică fragmentul pentru un începător. Prezice output-ul exact, inclusiv
spațiile și rândurile. Nu modifica fișierul.” Compară răspunsul cu o rulare reală.

**B. O propunere de cod limitată.** Pentru `miniapp.py` cere un mic fragment pentru
calculul sau formatarea totalului. Prompt: „Propune cel mult 5 linii Python, folosind
doar variabile, conversii și print. Totalul trebuie să aibă două zecimale.
Explică fiecare linie. Nu executa comenzi și nu modifica alte fișiere.”
Acceptă/adaptează numai după ce înțelegi. Verifică cele trei cazuri din LAB_02.md.

**C. Critică.** Cere o soluție pentru același calculator fără să precizezi inițial
conversia input-ului sau formatarea. Analizează propunerea: detectează un risc de
corectitudine sau nepotrivire pentru începători. Dacă este corectă, explică o limitare
(input invalid, lipsa cerințelor în prompt, complexitate) fără a inventa o eroare.
Rescrie promptul cu restricții și compară rezultatele.

În `raspunsuri/copilot.md` păstrezi promptul exact, fragmentul relevant al răspunsului,
ce ai acceptat/refuzat, motivul, testul și rezultatul observat. Scrie explicațiile
în cuvintele tale. Minimum o propunere trebuie refuzată sau adaptată justificat.

## Dacă nu ai acces la Copilot

Notează mesajul/problema și anunță profesorul. Poți termina Python și Git fără AI.
Pentru componenta Copilot participi la o demonstrație făcută de profesor/coleg,
fără partajarea conturilor, notezi „observat”, apoi verifici individual fragmentul.
Profesorul stabilește o recuperare pentru utilizarea individuală. Nu declara că ai
folosit Copilot dacă ai analizat numai un răspuns demonstrat.
