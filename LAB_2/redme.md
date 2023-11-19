# Testy Automatyczne - Przykładowy Projekt

## Opis Projektu

Projekt ten zawiera przykładowe scenariusze testowe przy użyciu Selenium w Pythonie. Scenariusze obejmują testowanie logowania i zakupu produktów na dwóch różnych stronach internetowych.

## Scenariusz Testowy 1: Zakup produktów na stronie saucedemo.com

**Kroki:**

1. Otwórz przeglądarkę Chrome.
2. Wejdź na stronę [https://www.saucedemo.com/](https://www.saucedemo.com/).
3. Zaloguj się używając poprawnych danych (nazwa użytkownika: problem_user, hasło: secret_sauce).
4. Sprawdź, czy logowanie przebiegło pomyślnie, poprzez sprawdzenie obecności koszyka zakupowego (element o id "shopping_cart_container").
5. Dodaj trzy produkty ("Sauce Labs Backpack", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie") do koszyka.
6. Sprawdź, czy liczba produktów w koszyku wynosi 3.
7. Zamknij przeglądarkę.

**Oczekiwane rezultaty:**

- Logowanie powinno przejść pomyślnie.
- Po dodaniu trzech produktów, liczba produktów w koszyku powinna być równa 3.
- Test kończy się pomyślnie.

---

## Scenariusz Testowy 2: Zmiana nazwiska użytkownika na stronie orangehrmlive.com

**Kroki:**

1. Otwórz przeglądarkę Edge.
2. Wejdź na stronę [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login).
3. Zaloguj się używając poprawnych danych (nazwa użytkownika: Admin, hasło: admin123).
4. Sprawdź, czy logowanie przebiegło pomyślnie, poprzez sprawdzenie obecności elementu nawigacyjnego (np. ikony menu).
5. Przejdź do sekcji zmiany informacji użytkownika.
6. Zmień nazwisko użytkownika na "Tester".
7. Sprawdź, czy zmiana nazwiska użytkownika została zapisana poprawnie.
8. Zamknij przeglądarkę.

**Oczekiwane rezultaty:**

- Logowanie powinno przejść pomyślnie.
- Zmiana nazwiska użytkownika na "Tester" powinna być zapisana poprawnie.
- Test kończy się pomyślnie.

---

Powyższe scenariusze testowe mają na celu pokrycie różnych funkcjonalności i operacji przeprowadzanych na dwóch różnych stronach internetowych. Ważne jest, aby zapewnić, że testowane funkcje działają zgodnie z oczekiwaniami.
