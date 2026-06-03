import streamlit as st
import pandas as pd
import joblib
st.title("Sales Prediction")
model,scaler = joblib.load(r"C:\Users\xvpow\ai2_20260408\ch17\sales_model_scaler.pkl")
tv_spend = st.number_input("輸入TV廣告支出",min_value=0.0)
radio_spend = st.number_input("輸入Radio廣告支出",min_value=0.0)
newspaper_spend = st.number_input("輸入NewsSaper廣告支出",min_value=0.0)

if st.button("預測銷售"):
    input_data = {
        "TV":tv_spend,
        "radio":radio_spend,
        "newspaper":newspaper_spend
    }
    input_df = pd.DataFrame([input_data])
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)
    st.write(f"預測銷售為:{prediction[0]}")
