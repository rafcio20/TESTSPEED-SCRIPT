# TESTSPEED-SCRIPT
new script
# 🚀 Internet Speed Logger (Python)

Skrypt w Pythonie do automatycznego testowania prędkości internetu i zapisywania wyników do pliku CSV. Idealny do monitorowania jakości połączenia w czasie i sprawdzania, czy dostawca internetu trzyma się obietnic.

---

## 🧩 Funkcje

- Test prędkości **download**, **upload** oraz **ping**
- Automatyczne wykonywanie pomiarów co określony czas (np. co 30 minut)
- Zapis wyników do pliku `speedtest_log.csv`
- Rejestrowanie czasu każdego pomiaru
- Gotowe do rozbudowy: wykresy, alerty, wysyłka logów

---

## 📦 Wymagania

Zainstaluj potrzebne biblioteki:

```bash
pip install speedtest-cli pandas
