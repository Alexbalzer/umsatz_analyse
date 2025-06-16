# 📊 Streamlit Apps: Umsatzanalyse & Statistik-Quiz

Dieses Repository enthält zwei interaktive Streamlit-Anwendungen zur Datenanalyse und Statistik:

---

## 1️⃣ Umsatzanalyse von Filialen

Diese Anwendung analysiert die Umsätze von Filialen anhand einer CSV-Datei.

### 🚀 Funktionen

- Einlesen von Umsatzdaten aus einer CSV-Datei
- Anzeige der wichtigsten Kennzahlen:
  - Gesamtumsatz
  - Arithmetisches Mittel (Durchschnitt)
  - Median
  - 3 kleinste und 3 größte Umsätze
- Einteilung in Umsatzklassen (Histogramm)
- Interaktive Visualisierung mit `matplotlib`

### 🔧 Starten

```bash
streamlit run app.py
```

---

## 2️⃣ Statistik-Quiz

Ein Lern-Quiz zur Wiederholung statistischer Grundbegriffe, z. B.:

- Skalenniveaus (nominal, ordinal, metrisch)
- Diskrete und stetige Merkmale
- Qualitative vs. quantitative Merkmale
- Fachbegriffe wie Grundgesamtheit, Merkmalsausprägung
- Richtig/Falsch-Fragen mit Feedback und Punktesystem

### 🧠 Lerninhalte

Das Quiz enthält über 30 Fragen aus Einführungsveranstaltungen zur Statistik – ideal zur Wiederholung oder Prüfungsvorbereitung.

### 💡 Funktionen

- Multiple-Choice-Fragen mit direktem Feedback
- Automatische Auswertung und Punktevergabe
- Aufgaben sind in Abschnitte unterteilt (Skalenniveau, Merkmale, Begriffe etc.)

### 🔧 Starten

```bash
streamlit run quiz_app.py
```

---

## 🧪 Installation & Setup

### Windows

```bash
# Python 3 installieren (falls noch nicht vorhanden)
git clone git@github.com:Olexandr-Andriyenko/abschlussprojekt.git <project_name>
cd <project_name>
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux

```bash
# Python 3 installieren (falls noch nicht vorhanden)
git clone git@github.com:Olexandr-Andriyenko/abschlussprojekt.git <project_name>
cd <project_name>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 📁 Struktur

```
<project_name>/
├── app.py         # Umsatzanalyse-App
├── quiz_app.py    # Statistik-Quiz
├── requirements.txt
└── README.md      # Diese Datei
```

---

## 📝 Hinweis

Beide Apps sind unabhängig voneinander ausführbar. Du kannst sie je nach Lernziel oder Analysefokus einzeln starten.