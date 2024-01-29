# Testowanie Wydajnościowe za pomocą Apache JMeter

## 1. Obiekt Testowy: Strona saucedemo.com

### Opis Testu
Test ma na celu ocenę wydajności strony internetowej [saucedemo.com](https://www.saucedemo.com/). W tym teście użyto narzędzia Apache JMeter do symulacji obciążenia.

### Ustawienia Testu
- Liczba Użytkowników: 1000
- Okres Rozruchu: 5 sekund
- Powtórzenia: 4

#### Konfiguracja Testu
![Konfiguracja Testu](https://github.com/Nougat00/TAU/blob/98bb84a37ed83ec5505c87c3f59c19b0f1c32d4c/LAB_5/img/Zrzut%20ekranu%202024-01-29%20232546.png)

#### Wykres Wydajności
![Wykres Wydajności](https://github.com/Nougat00/TAU/blob/0d842ec84ad9430a6f135b859de69fc7c70a5530/LAB_5/img/Zrzut%20ekranu%202024-01-29%20234053.png)
   - Wykres wskazuje, że strona stała się bardzo nie stabilna w okolicy 1500 zapytań, co spowodowało znaczny spadek wydajności.

#### Rezultaty w tabeli
![Raport w tabeli](https://github.com/Nougat00/TAU/blob/0d842ec84ad9430a6f135b859de69fc7c70a5530/LAB_5/img/Zrzut%20ekranu%202024-01-29%20232603.png)
   - Raport w tabeli pokazuje że nie wystąpiły żadne błędy podczas wywoływania testu.

#### Raport zagregowany
![Raport zagregowany](https://github.com/Nougat00/TAU/blob/0d842ec84ad9430a6f135b859de69fc7c70a5530/LAB_5/img/Zrzut%20ekranu%202024-01-29%20232611.png)
   - Raport zagregowany pokazuje, że mimo spadku wydajności, nie wystąpiły żadne błędy podczas testu.

### Wnioski
Test wydajnościowy jednoznacznie wskazuje na potrzebę optymalizacji strony, zwłaszcza w kontekście obsługi większej liczby użytkowników. 
Pomimo stabilnego działania strony w normalnych warunkach, test wydajnościowy ujawnił obszary do poprawy, co może przyczynić się do lepszej jakości obsługi strony przy większym obciążeniu.




