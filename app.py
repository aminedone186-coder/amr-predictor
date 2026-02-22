import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AMR Predictor", page_icon="🦠", layout="wide")
st.title("🧬 Antibiotic Resistance Predictor")
st.markdown("Predict resistance from gene presence data")

with st.sidebar:
    st.header("⚙️ Settings")
    antibiotic = st.selectbox("Select Antibiotic", ["Ciprofloxacin", "Ampicillin", "Gentamicin", "Ceftazidime", "Cefotaxime"])

tab1, tab2, tab3 = st.tabs(["📤 Input Data", "📊 Prediction", "📚 Tutorial"])

with tab1:
    st.header("Enter Gene Presence Data")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Upload File")
        uploaded = st.file_uploader("Upload CSV (0/1 per gene)", type=['csv'])
        if uploaded:
            st.dataframe(pd.read_csv(uploaded).head())
    with col2:
        st.subheader("Manual Entry")
        genes = ["gyrA","parC","ampC","blaTEM","blaCTX-M","tetA","aac(3)-II","dfrA"]
        for g in genes:
            st.checkbox(g, key=g)

with tab2:
    st.header("Prediction Results")
    if st.button("🔮 Predict"):
        # Demo prediction – replace with your real model later
        conf = {"Ciprofloxacin":0.87, "Ampicillin":0.91, "Gentamicin":0.84, "Ceftazidime":0.79, "Cefotaxime":0.82}
        conf_val = conf[antibiotic]
        pred = "RESISTANT" if conf_val > 0.5 else "SUSCEPTIBLE"
        st.metric("Prediction", pred)
        st.metric("Confidence", f"{conf_val*100:.0f}%")
        st.progress(conf_val)
        # Feature importance
        imp = pd.DataFrame({'Gene':['gyrA','parC','ampC','blaTEM','tetA'], 'Importance':[0.42,0.28,0.15,0.10,0.05]})
        fig, ax = plt.subplots()
        ax.barh(imp['Gene'], imp['Importance'])
        ax.set_xlabel('Importance')
        st.pyplot(fig)
        st.info("Demo mode – replace with your trained model")

with tab3:
    st.markdown("Follow [PLOS tutorial](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010958) to train your own model.")

st.markdown("---")
st.markdown("Gomel State Medical University")
