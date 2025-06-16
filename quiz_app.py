import streamlit as st

st.set_page_config(page_title="Statistik-Quiz", page_icon="📊")
st.title("📊 Statistik-Quiz: Skalenniveaus & Merkmalsarten")
st.write("Beantworte die folgenden Fragen. Jede richtige Antwort gibt einen Punkt.")

# Richtige Antworten
richtige_antworten = {
    # Aufgabe 1
    "q1": "Metrisch",
    "q2": "Nominal",
    "q3": "Ordinal",
    "q4": "Metrisch",
    "q5": "Nominal",
    "q6": "Ordinal",
    "q7": "Metrisch",
    "q8": "Nominal",
    "q9": "Metrisch",
    "q10": "Ordinal",
    # Aufgabe 2
    "q11": "Stetig",
    "q12": "Stetig",
    "q13": "Diskret",
    "q14": "Stetig",
    "q15": "Stetig",
    "q16": "Diskret",
    # Aufgabe 3
    "q17": "Falsch",
    "q18": "Falsch",
    "q19": "Falsch",
    "q20": "Falsch",
    "q21": "Richtig",
    "q22": "Richtig",
    "q23": "Falsch",
    # Aufgabe 4
    "q24": "Grundgesamtheit",
    "q25": "Merkmalsträger",
    "q26": "Merkmal",
    "q27": "Merkmalsausprägung",
    # Aufgabe 6
    "q28": "Richtig",
    "q29": "Falsch",
    "q30": "Falsch",
    "q31": "Richtig",
    # Aufgabe 7
    "q32": "Qualitativ - Nominal",
    "q33": "Quantitativ - Metrisch",
    "q34": "Quantitativ - Metrisch",
    "q35": "Qualitativ - Nominal",
    "q36": "Quantitativ - Ordinal",
    "q37": "Quantitativ - Metrisch",
    "q38": "Quantitativ - Diskret"
}

fragen = [
    # Aufgabe 1
    ("1: Körpertemperatur in °C", ["Nominal", "Ordinal", "Metrisch"]),
    ("2: Augenfarbe", ["Nominal", "Ordinal", "Metrisch"]),
    ("3: Kundenzufriedenheit (Skala: unzufrieden – neutral – zufrieden)", ["Nominal", "Ordinal", "Metrisch"]),
    ("4: Gewicht in kg", ["Nominal", "Ordinal", "Metrisch"]),
    ("5: Blutgruppe", ["Nominal", "Ordinal", "Metrisch"]),
    ("6: Platzierung im Wettkampf", ["Nominal", "Ordinal", "Metrisch"]),
    ("7: Alter in Jahren", ["Nominal", "Ordinal", "Metrisch"]),
    ("8: Beruf", ["Nominal", "Ordinal", "Metrisch"]),
    ("9: Schuhgröße", ["Nominal", "Ordinal", "Metrisch"]),
    ("10: Schmerzempfinden (leicht – mittel – stark)", ["Nominal", "Ordinal", "Metrisch"]),
    # Aufgabe 2
    ("11: Einkommen in €", ["Diskret", "Stetig"]),
    ("12: Körpergröße in cm", ["Diskret", "Stetig"]),
    ("13: Anzahl der Autos pro Haushalt", ["Diskret", "Stetig"]),
    ("14: Temperatur in Kelvin", ["Diskret", "Stetig"]),
    ("15: Zeitdauer in Sekunden", ["Diskret", "Stetig"]),
    ("16: Anzahl von Toren in einem Fußballspiel", ["Diskret", "Stetig"]),
    # Aufgabe 3
    ("17: Das Alter einer Person ist ordinal skaliert.", ["Richtig", "Falsch"]),
    ("18: Die Augenfarbe ist ein metrisches Merkmal.", ["Richtig", "Falsch"]),
    ("19: Einkommen ist ein qualitatives Merkmal.", ["Richtig", "Falsch"]),
    ("20: Schuhgrößen sind stetige, metrische Merkmale.", ["Richtig", "Falsch"]),
    ("21: Blutgruppen sind nominale Merkmale.", ["Richtig", "Falsch"]),
    ("22: Eine Bewertungsskala von 1 bis 5 (z. B. Schulnoten) ist ordinal.", ["Richtig", "Falsch"]),
    ("23: Temperatur in °C erlaubt Verhältnisbildungen (z. B. doppelt so warm).", ["Richtig", "Falsch"]),
    # Aufgabe 4
    ("24: Alle Studierenden in Deutschland", ["Grundgesamtheit", "Merkmalsträger", "Merkmal", "Merkmalsausprägung"]),
    ("25: Eine einzelne Studentin", ["Grundgesamtheit", "Merkmalsträger", "Merkmal", "Merkmalsausprägung"]),
    ("26: Rauchverhalten", ["Grundgesamtheit", "Merkmalsträger", "Merkmal", "Merkmalsausprägung"]),
    ("27: Raucht regelmäßig / Nichtraucher", ["Grundgesamtheit", "Merkmalsträger", "Merkmal", "Merkmalsausprägung"]),
    # Aufgabe 6
    ("28: Eine Merkmalsausprägung beschreibt eine bestimmte Eigenschaft eines einzelnen Merkmalsträgers.", ["Richtig", "Falsch"]),
    ("29: Ein Merkmal kann nur quantitativ sein.", ["Richtig", "Falsch"]),
    ("30: Die Grundgesamtheit ist gleichbedeutend mit der Stichprobe.", ["Richtig", "Falsch"]),
    ("31: Der Verknüpfungsfehlschluss entsteht, wenn Menschen mehrere Ereignisse gleichzeitig für wahrscheinlicher halten als eines davon allein.", ["Richtig", "Falsch"]),
    # Aufgabe 7
    ("32: Geschlecht", ["Qualitativ - Nominal", "Quantitativ - Ordinal", "Quantitativ - Metrisch"]),
    ("33: Körpergröße", ["Qualitativ - Nominal", "Quantitativ - Ordinal", "Quantitativ - Metrisch"]),
    ("34: Beliebtheit eines Lehrers (0–10)", ["Qualitativ - Nominal", "Quantitativ - Ordinal", "Quantitativ - Metrisch"]),
    ("35: Beruf", ["Qualitativ - Nominal", "Quantitativ - Ordinal", "Quantitativ - Metrisch"]),
    ("36: Schulnote (z. B. 1 bis 6)", ["Qualitativ - Nominal", "Quantitativ - Ordinal", "Quantitativ - Metrisch"]),
    ("37: Temperatur in °C", ["Qualitativ - Nominal", "Quantitativ - Ordinal", "Quantitativ - Metrisch"]),
    ("38: Anzahl Kinder pro Familie", ["Qualitativ - Nominal", "Quantitativ - Diskret", "Quantitativ - Stetig"])
]

antworten = {}
punkte = 0

for i, (frage, optionen) in enumerate(fragen):
    key = f"q{i+1}"
    antworten[key] = st.radio(f"{i+1}. {frage}", optionen, key=key)

if st.button("Antworten auswerten"):
    for key, user_value in antworten.items():
        korrekt = richtige_antworten[key]
        if user_value == korrekt:
            st.success(f"{key}: Richtig! ({korrekt})")
            punkte += 1
        else:
            st.error(f"{key}: Falsch. Richtige Antwort: {korrekt}")

    st.markdown("---")
    st.subheader(f"🎯 Gesamtpunktzahl: {punkte} von {len(fragen)}")

