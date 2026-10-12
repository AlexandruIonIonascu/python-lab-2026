# Python: de la fișier sursă la output

Python este un limbaj de programare. Fișierul `.py` conține instrucțiuni scrise
în acest limbaj. Interpretorul Python este programul care execută instrucțiunile.
În Codespaces, comanda `python app.py` pornește interpretorul cu fișierul ca argument.
Un program Python poate automatiza calcule, analiza date sau construi aplicații;
primele noastre aplicații sunt aplicații de terminal, fără interfață grafică.

Într-un script simplu, instrucțiunile se execută în ordine. Nu învăța că Python
„citește întotdeauna doar câte o linie”: în CPython sursa este compilată în bytecode
înainte de execuție. O eroare de sintaxă în fișier poate împiedica orice afișare.

## Cum funcționează `print`

`print` este o funcție predefinită. În mod obișnuit scrie text pe output-ul standard
(`stdout`), pe care terminalul îl afișează. Nu salvează codul, nu face commit,
nu creează implicit un fișier și nu deschide o pagină web.

```python
print("Salut!")
print(2 + 3)
print("2" + "3")
```

Output:

```text
Salut!
5
23
```

Ghilimelele delimitează un șir de caractere (`str`); nu se afișează. `2` este un
număr întreg (`int`); `"2"` este text. `+` adună numere, dar concatenează două șiruri.
O linie care începe cu `#` este comentariu și nu produce output.
`print()` fără argumente produce implicit o linie goală.

| Fragment | Output | Explicație |
| --- | --- | --- |
| `print("A", "B")` | `A B` | Separator implicit: spațiu |
| `print("A", "B", sep="|")` | `A|B` | Separator explicit între argumente |
| `print("A", end=""); print("B")` | `AB` pe aceeași linie | Primul apel nu încheie linia |
| `print("A\nB")` | `A` și `B` pe linii diferite | `\n` din șir reprezintă un rând nou |

Fără `end` explicit, `print` adaugă `\n` la final. Pentru laborator scrie apelurile
pe linii separate; punctul și virgula din tabel doar comprimă exemplul.
`sep` și `end` sunt argumente cu nume și trebuie să fie șiruri (sau `None`).

## Variabile și expresii

```python
alias = "Ada"
cantitate = 2
pret = 12.5
total = cantitate * pret
print(f"Total: {total:.2f}")
```

`=` atribuie o valoare unui nume. `*` înmulțește. `12.5` este un număr cu virgulă
mobilă (`float`), scris cu punct în Python. Un f-string introduce valori în text:
`{total:.2f}` afișează exact două zecimale. `print` afișează rezultatul calculului;
calculul se face în expresie, nu pentru că `print` ar fi un calculator special.

## `input`: aplicația citește de la utilizator

```python
alias = input("Alias: ")
print(f"Salut, {alias}!")
```

Programul așteaptă până tastezi răspunsul și apeși Enter în terminal.
`input` întoarce text. Pentru calcule folosești conversii:

```python
cantitate = int(input("Cantitate: "))
pret = float(input("Pret unitar: "))
```

`int("2")` produce 2; `float("12.5")` produce 12.5.
`int("doua")` și `float("12,5")` produc `ValueError`. Cerința de bază presupune
input valid; validarea input-ului este un exercițiu opțional.
În REPL, expresia `2 + 3` își afișează rezultatul automat; aceeași expresie singură
într-un script nu afișează nimic. În script ai nevoie de `print(2 + 3)`.

## Trei erori pe care le investighezi

| Eroare | Exemplu | Ce verifici |
| --- | --- | --- |
| `SyntaxError` | O paranteză neînchisă | Sintaxa; fișierul poate să nu ruleze deloc |
| `NameError` | `print(mesaj)` fără definirea lui `mesaj` | Nume, ghilimele, ordinea atribuirilor |
| `TypeError` | `"Total: " + 5` | Tipuri incompatibile; folosește conversie, virgulă sau f-string |

Citește ultima linie a erorii, apoi numele fișierului și numărul liniei.
Indentarea contează pentru blocuri Python. La început folosim instrucțiuni la
nivelul de bază, fără spații la începutul liniei. Python distinge majusculele:
`print` funcționează, `Print` este alt nume.

Practică: întâi prezici rezultatul, apoi rulezi, compari și explici diferența.
