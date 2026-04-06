import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_model.pkl")

st.title("FraudSense: Smart Financial Fraud Detection")


st.markdown(" Please enter the details of the transaction & Click on the Predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["Payment", "Transfer", "Cash_Out", "Debit", "Cash_In"])
amount = st.number_input("Amount", min_value=0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin i.e. Sender's Old Balance", min_value = 0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance Origin i.e. Sender's New Balance", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance Destination i.e. Receiver's Old Balance", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance Destination i.e. Receiver's New Balance", min_value = 0.0, value = 0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type.upper(),
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("The transaction is predicted to be fraud.")
    else:
        st.success("The transaction is predicted to be legitimate.")
