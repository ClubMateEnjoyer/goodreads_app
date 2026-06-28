import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Visualisierungen", page_icon="📈")
st.title("📈 Explorative Datenanalyse")

@st.cache_data
def load_data():
    return pd.read_csv('data/goodreads_works_cleaned.csv')

df = load_data()

# Auswahl-Menü für den Plot
plot_type = st.selectbox(
    "Wähle eine Visualisierung:",
    [
        "Verteilung der Ratings (Histogramm)", 
        "Einfluss der Buchlänge (Boxplot)", 
        "Einfluss der Popularität (Boxplot)"
    ]
)

st.markdown("---")

if plot_type == "Verteilung der Ratings (Histogramm)":
    st.subheader("Verteilung der durchschnittlichen Bewertungen (avg_rating)")
    st.markdown("Das Histogramm zeigt eine annähernde Normalverteilung der Daten, wobei der Großteil der Bewertungen zwischen 3,8 und 4,2 Sternen liegt.")
    
    # Interaktives Plotly Histogramm
    fig = px.histogram(
        df, 
        x='avg_rating', 
        nbins=30, 
        opacity=0.75,
        color_discrete_sequence=['#636EFA'],
        labels={'avg_rating': 'Durchschnittliche Bewertung', 'count': 'Häufigkeit'}
    )
    fig.update_layout(bargap=0.1)
    
    st.plotly_chart(fig, use_container_width=True)

elif plot_type == "Einfluss der Buchlänge (Boxplot)":
    st.subheader("Einfluss der Buchlänge auf die Bewertung")
    st.markdown("Lange Bücher ('long') werden tendenziell leicht besser bewertet als kurze oder mittellange Werke. Bei kürzeren Büchern gibt es mehr Ausreißer nach unten.")
    
    # Interaktiver Plotly Boxplot
    fig = px.box(
        df, 
        x='length_category', 
        y='avg_rating', 
        color='length_category',
        category_orders={"length_category": ["short", "medium", "long"]},
        labels={
            'length_category': 'Buchlänge (Kategorie)', 
            'avg_rating': 'Durchschnittliche Bewertung'
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif plot_type == "Einfluss der Popularität (Boxplot)":
    st.subheader("Einfluss der Popularität auf die Bewertung")
    st.markdown("Sehr populäre Bücher weisen im Durchschnitt höhere Ratings auf als reine Nischen-Titel. Die Streuung in den negativen Bereich verringert sich mit zunehmender Bekanntheit.")
    
    # Interaktiver Plotly Boxplot
    fig = px.box(
        df, 
        x='popularity_category', 
        y='avg_rating', 
        color='popularity_category',
        category_orders={"popularity_category": ["niche", "known", "popular"]},
        labels={
            'popularity_category': 'Popularität (Kategorie)', 
            'avg_rating': 'Durchschnittliche Bewertung'
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)