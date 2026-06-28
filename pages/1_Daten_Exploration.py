import streamlit as st
import pandas as pd

st.set_page_config(page_title="Daten Exploration", page_icon="🔍")
st.title("🔍 Daten Exploration")

@st.cache_data
def load_data():
    return pd.read_csv('data/goodreads_works_cleaned.csv')

df = load_data()

# Sidebar: Filter Optionen
st.sidebar.header("Filter Optionen")

min_pages = int(df['num_pages'].min())
max_pages = int(df['num_pages'].max())

page_range = st.sidebar.slider(
    "Seitenanzahl filtern:",
    min_value=min_pages,
    max_value=max_pages,
    value=(min_pages, max_pages)
)

# Ein Dropdown für die Popularität
popularity_filter = st.sidebar.multiselect(
    "Popularität wählen:",
    options=df['popularity_category'].unique(),
    default=df['popularity_category'].unique()
)

# Daten filtern
filtered_df = df[
    (df['num_pages'] >= page_range[0]) & 
    (df['num_pages'] <= page_range[1]) &
    (df['popularity_category'].isin(popularity_filter))
]

# Tab für die Top 5 Listen
tab1, tab2, tab3 = st.tabs(["📊 Gefilterte Daten", "📈 Statistische Zusammenfassung", "🏆 Top 5 Listen"])

with tab1:
    st.write(f"Zeige **{len(filtered_df)}** von **{len(df)}** Büchern an.")
    st.dataframe(filtered_df)

with tab2:
    st.dataframe(filtered_df.describe())

with tab3:
    if len(filtered_df) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Top 5 nach Bewertung ⭐️")
            # Die 5 Bücher mit dem höchsten avg_rating holen
            top5_rating = filtered_df.nlargest(5, 'avg_rating')[['original_title', 'author', 'avg_rating', 'num_pages']]
            st.dataframe(top5_rating, hide_index=True)
            
        with col2:
            st.subheader("Top 5 nach Bekanntheit 📣")
            # Die 5 Bücher mit den meisten ratings_count holen
            top5_pop = filtered_df.nlargest(5, 'ratings_count')[['original_title', 'author', 'ratings_count', 'avg_rating']]
            st.dataframe(top5_pop, hide_index=True)
    else:
        st.warning("Keine Bücher für die ausgewählten Filter gefunden.")