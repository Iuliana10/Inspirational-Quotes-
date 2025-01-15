#Inspirational Quotes

**Acesta este un proiect Python cu interfață grafică (GUI) care afișează citate inspiraționale obținute de pe un site web. Utilizatorii pot vizualiza citate aleatorii, pot reîncărca citate noi și pot urmări citatele deja afișate.
Site-ul: https://citate.top/categorii/inspirationale/
---

#Caracteristici

- Afișează citate inspiraționale aleatorii.
- Permite reîncărcarea și obținerea de citate noi.
- Ține evidența citatelor afișate anterior.
- Utilizează o imagine personalizată ca fundal pentru interfața grafică.
---
#Cerinte

Pentru a rula acest proiect, ai nevoie de următoarele biblioteci:
- requests: Pentru obținerea datelor de pe internet.
- bs4 (BeautifulSoup): Pentru parsarea HTML. 
- tkinter: Pentru crearea interfeței grafice. 
- PIL (Pillow): Pentru manipularea imaginilor.

Instalează bibliotecile necesare folosind comanda: pip install requests beautifulsoup4 pillow.

---
#Cum se ruleaza

- Salvează imaginea de fundal în același director cu scriptul sau actualizează calea către imagine în cod.
- Rulează scriptul folosind comanda: python inspirational_quotes.py.

---
#Funcții:

- get_citate(): Obține citate inspiraționale de pe site-ul citate.top. Dacă cererea nu reușește, afișează o casetă de eroare. 
- show_random_citat(): Afișează un citat aleatoriu din lista obținută, îl elimină din citatele disponibile și îl adaugă în lista citatelor utilizate. Actualizează eticheta cu citate folosite folosind text împărțit pe linii. 
- wrap_text(text, line_length=80): Împarte citatele lungi în mai multe linii pentru a se încadra în fereastră. 
- refresh_citate(): Reîncarcă citatele de pe site și golește lista citatelor utilizate.
---
#Componente GUI

- root: Fereastra principală a aplicației. 
- background_label: Afișează imaginea de fundal. 
- citat_label: Etichetă pentru afișarea citatului curent. 
- random_button: Buton pentru afișarea unui citat aleatoriu. 
- refresh_button: Buton pentru reîncărcarea citatelor. 
- used_label: Etichetă pentru afișarea citatelor utilizate anterior.