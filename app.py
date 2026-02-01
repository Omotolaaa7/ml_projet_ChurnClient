import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load('notebooks/churn_model_pipeline.pkl')

st.title("Prédiction du churn des clients")
st.write("""Cette application prédit si un client va churner (quitter le service) ou non. 
        Veuillez entrer les informations du client et cliquez sur **Prédire** :
        """)

# Formulaire pour les entrées utilisateur

st.header("Informations du client")

# Variables numériques
tenure_months = st.number_input("Ancienneté du client (mois)", min_value=0, max_value=100)
monthly_charges = st.number_input("Montant mensuel ", min_value=0.0, max_value=1000.0)
total_charges = st.number_input("Total des charges ", min_value=0.0, max_value=50000.0)

# Variables catégorielles
gender = st.selectbox("Genre", ["Male", "Female"])
senior_citizen = st.selectbox("Client senior", ["Yes", "No"])
partner = st.selectbox("Partenaire", ["Yes", "No"])
dependents = st.selectbox("Personnes à charge", ["Yes", "No"])
phone_service = st.selectbox("Service téléphonique", ["Yes", "No"])
multiple_lines = st.selectbox("Lignes multiples", ["No phone service", "No", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.selectbox("Streaming films", ["Yes", "No"])
contract = st.selectbox("Type de contrat", ["Month-to-month", "One year", "Two year"])
tech_support = st.selectbox("Support technique", ["Yes", "No"])
online_security = st.selectbox("Sécurité en ligne", ["Yes", "No"])
online_backup = st.selectbox("Sauvegarde en ligne", ["Yes", "No"])
device_protection = st.selectbox("Protection des appareils", ["Yes", "No"])
paperless_billing = st.selectbox("Facturation papier", ["Yes", "No"])
payment_method = st.selectbox("Méthode de paiement", 
                              ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
internet_service = st.selectbox("Type d'Internet", ["DSL", "Fiber optic", "No"])

# On crée un DataFrame avec les entrées utilisateur
input_data = pd.DataFrame({
    'tenure_months': [tenure_months],
    'monthly_charges': [monthly_charges],
    'total_charges': [total_charges],
    'gender': [gender],
    'senior_citizen': [senior_citizen],
    'partner': [partner],
    'dependents': [dependents],
    'phone_service': [phone_service],
    'multiple_lines': [multiple_lines],
    'streaming_tv': [streaming_tv],
    'streaming_movies': [streaming_movies],
    'contract': [contract],
    'tech_support': [tech_support],
    'online_security': [online_security],
    'online_backup': [online_backup],
    'device_protection': [device_protection],
    'paperless_billing': [paperless_billing],
    'payment_method': [payment_method],
    'internet_service': [internet_service]
})

if st.button("Prédire"):
    prediction = pipeline.predict(input_data)[0]
    proba = pipeline.predict_proba(input_data)[0][1]
    
    st.subheader("Résultat de la prédiction")
    if prediction == 1:
        st.write("Le client va churner (quitter le service).")
    else:
        st.write("Le client ne va pas churner (rester avec le service).")
        
    st.write(f"Probabilité de churn : {proba:.2f}")
    st.info("Interprétation : Une probabilité élevée indique un risque accru de churn. On peut envisager des actions de rétention pour ces clients.")