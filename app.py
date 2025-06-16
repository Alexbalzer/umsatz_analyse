import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titel
st.title("📊 Umsatzanalyse der Filialen")

# CSV-Datei einlesen
uploaded_file = st.file_uploader("Wähle die CSV-Datei mit den Umsatzdaten aus", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=";", decimal=",")

    # Umsatzspalte validieren
    if "Umsatz" not in df.columns:
        st.error("Die CSV-Datei muss eine Spalte namens 'Umsatz' enthalten.")
    else:
        st.subheader("Datenvorschau")
        st.dataframe(df)

        # Grundlegende Kennzahlen
        gesamtumsatz = df["Umsatz"].sum()
        mittelwert = df["Umsatz"].mean()
        median = df["Umsatz"].median()
        kleinste = df.nsmallest(3, "Umsatz")
        groesste = df.nlargest(3, "Umsatz")

        st.subheader("Statistische Kennzahlen")
        st.metric("Gesamtumsatz", f"{gesamtumsatz:.2f} (in 100.000 €)")
        st.metric("Durchschnitt", f"{mittelwert:.2f} (in 100.000 €)")
        st.metric("Median", f"{median:.2f} (in 100.000 €)")

        st.subheader("Drei kleinste Umsätze")
        st.dataframe(kleinste)

        st.subheader("Drei größte Umsätze")
        st.dataframe(groesste)

        # Klassen für Histogramm
        bins = np.arange(0, df["Umsatz"].max() + 1, 1)
        df["Klasse"] = pd.cut(df["Umsatz"], bins=bins, right=False)
        haeufigkeit = df["Klasse"].value_counts().sort_index()

        # Balkendiagramm
        st.subheader("Histogramm der Umsatzklassen")
        fig, ax = plt.subplots()
        ax.bar(haeufigkeit.index.astype(str), haeufigkeit.values, color='skyblue', edgecolor='black')
        ax.set_xlabel("Umsatzklassen (in 100.000 €)")
        ax.set_ylabel("Anzahl Filialen")
        ax.set_title("Verteilung der Umsätze")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
else:
    st.info("Bitte lade eine CSV-Datei hoch. Die Datei muss eine Spalte namens 'Umsatz' enthalten.")
