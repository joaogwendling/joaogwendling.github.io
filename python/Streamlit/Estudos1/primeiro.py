import streamlit as st

st.title("Calculadora de IMC")

altura = st.slider("Altura", 0.00, 2.50, value=1.70)
peso = st.slider("Peso", 0.0, 300.0, value=90.0)

botao = st.button("Calcular")

if botao:
    IMC = peso/(altura**2)
    st.markdown(f"Seu IMC é: **{IMC}**")