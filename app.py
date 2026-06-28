import streamlit as st
import pandas as pd

# 1. Page Config (muss immer ganz oben stehen!)
st.set_page_config(
    page_title="Goodreads Buchanalyse", 
    page_icon="📚", 
    layout="wide"
)

# 2. Daten laden (mit Cache, damit die App schnell bleibt)
@st.cache_data
def load_data():
    # Achte darauf, dass der Dateiname exakt mit deiner CSV im data/ Ordner übereinstimmt
    return pd.read_csv('data/goodreads_works_cleaned.csv')

def main():
    st.title("📚 Goodreads Buchanalyse Dashboard")
    st.markdown("""
    Willkommen zur interaktiven Analyse literarischer Erfolgsfaktoren! 
    Diese App untersucht, wie sich Buchmerkmale wie Seitenanzahl und Popularität auf die Nutzerbewertungen auswirken.
    Grundlage hierfür ist ein Datensatz des Online-Buch_Portals Goodreads.
    👈 **Wähle eine Seite in der Sidebar, um tiefer in die Daten einzutauchen.**
    """)

    # Daten laden
    df = load_data()

    st.markdown("---")
    st.subheader("Kurzübersicht des Datensatzes")

    # Quick Stats
    col1, col2, col3 = st.columns(3)
    col1.metric("Anzahl Bücher (bereinigt)", len(df))
    col2.metric("Durchschn. Bewertung", f"{df['avg_rating'].mean():.2f} ⭐️")
    col3.metric("Durchschn. Seitenanzahl", f"{df['num_pages'].mean():.0f}")

    st.markdown("### Ein Blick in die Daten")
    st.dataframe(df.head(10))

if __name__ == '__main__':
    main()