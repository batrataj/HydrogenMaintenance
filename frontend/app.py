import streamlit as st
import requests

st.title("Hydrogen Maintenance Prediction")

temperature = st.number_input("درجة الحرارة")
pressure = st.number_input("الضغط")
flow_rate = st.number_input("معدل التدفق")

if st.button("تنبؤ"):
    data = {'temperature': temperature, 'pressure': pressure, 'flow_rate': flow_rate}
    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    st.write("التنبؤ:", response.json()['prediction'])
