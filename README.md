# Goodreads Data Explorer & Rating Prediction

Eine interaktive Web-Applikation, entwickelt mit **Streamlit**, zur explorativen Datenanalyse (EDA) und Machine-Learning-basierten Vorhersage von Buchbewertungen. Das Projekt entstand im Rahmen des Kurses "Data Science und Machine Learning mit Python".

## Features

Die App besteht aus drei Hauptkomponenten:
1. ** Daten Exploration:** Interaktives Filtern eines bereinigten Goodreads-Datensatzes nach Seitenanzahl und Popularität. Dynamische Generierung von Top-5-Listen (nach Bewertung und Bekanntheit).
2. ** Explorative Datenanalyse (EDA):** Visuelle Untersuchung der Datenverteilung mittels interaktiver `Plotly`-Diagramme (Histogramme zur Rating-Verteilung, Boxplots zum Einfluss von Buchlänge und Popularität).
3. ** ML Rating Prediction:** Ein interaktives Interface zum Training eines **Random Forest Regressors** (`scikit-learn`). Nutzer können eigene Parameter (Seitenanzahl, Anzahl der Bewertungen, Text-Reviews) eingeben, um das zu erwartende Rating eines Buches vorherzusagen.

## Tech Stack

- **Sprache:** Python 3.x
- **UI Framework:** Streamlit
- **Datenverarbeitung:** Pandas
- **Visualisierung:** Plotly Express
- **Machine Learning:** Scikit-Learn

## Installation & Setup

1. **Repository klonen:**
   ```bash
   git clone [https://github.com/DEIN_USERNAME/DEIN_REPO_NAME.git](https://github.com/DEIN_USERNAME/DEIN_REPO_NAME.git)
   cd DEIN_REPO_NAME
   pip install -r requirements.txt
   streamlit run app.py
