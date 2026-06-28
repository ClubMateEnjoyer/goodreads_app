import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="ML Prediction", page_icon="🤖", layout="wide")
st.title("🤖 Rating Prediction")

@st.cache_data
def load_data():
    return pd.read_csv('data/goodreads_works_cleaned.csv')

df = load_data()

st.markdown("""
Hier kannst du das in Woche 9 entwickelte **Random Forest Regressor** Modell trainieren und eigene Vorhersagen für Buchbewertungen treffen.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("1. Modell Training")
    
    if st.button("Modell jetzt trainieren"):
        with st.spinner("Modell wird trainiert..."):
            # 1. Features (X) und Target (y) definieren
            X = df[['num_pages', 'ratings_count', 'text_reviews_count']]
            y = df['avg_rating']
            
            # 2. Train/Test Split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # 3. Modell initialisieren und trainieren
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # 4. Vorhersagen auf den Testdaten
            y_pred = model.predict(X_test)
            
            # 5. Modell evaluieren
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            # Modell im Session State speichern
            st.session_state['trained_model'] = model
            st.session_state['mse'] = mse
            st.session_state['r2'] = r2
            
        st.success("Training erfolgreich abgeschlossen!")
        
    # Ergebnisse anzeigen, falls Modell trainiert ist
    if 'trained_model' in st.session_state:
        st.subheader("Evaluationsergebnisse:")
        st.metric("Mean Squared Error (MSE)", f"{st.session_state['mse']:.4f}")
        st.metric("R²-Score", f"{st.session_state['r2']:.4f}")
        st.info("Hinweis: Der niedrige R²-Score zeigt, dass sich qualitative Buchbewertungen nur schwer allein aus quantitativen Metriken vorhersagen lassen.")

with col2:
    st.header("2. Vorhersage treffen")
    
    if 'trained_model' in st.session_state:
        st.write("Gib Buch-Eigenschaften ein, um das voraussichtliche Rating zu berechnen:")
        
        # Input-Felder
        input_pages = st.number_input("Seitenanzahl (num_pages)", min_value=1, max_value=2000, value=300)
        input_ratings = st.number_input("Anzahl der Bewertungen (ratings_count)", min_value=0, max_value=5000000, value=10000)
        input_reviews = st.number_input("Anzahl der Text-Reviews (text_reviews_count)", min_value=0, max_value=50000, value=500)
        
        if st.button("Rating vorhersagen"):
            model = st.session_state['trained_model']
            
            # Neuen DataFrame für die Vorhersage erstellen
            input_data = pd.DataFrame({
                'num_pages': [input_pages],
                'ratings_count': [input_ratings],
                'text_reviews_count': [input_reviews]
            })
            
            prediction = model.predict(input_data)[0]
            
            st.success(f"Das prognostizierte Rating liegt bei: **{prediction:.2f} Sternen** ⭐️")
    else:
        st.info("👈 Bitte trainiere zuerst das Modell auf der linken Seite!")