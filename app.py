
# (['bed', 'bath', 'house_size']

import streamlit as st 
import joblib
import numpy as np

scaler = joblib.load("Scaler.pkl")
model = joblib.load("model.pkl")

st.title("Real Estate Price Prediction")


with st.form(key="form"):
    bed = st.number_input("Enter Number of  Beds : ",value=2,step=1)
    bath = st.number_input(" Enter number of Bathrooms : ",value=1,step=1)
    size = st.number_input("Enter Size : ",value=1000,step = 50)
    
    x = [bed,bath,size]
    st.divider()
    submit_btn = st.form_submit_button("Predict")
    
    if submit_btn:
        x1 = np.array([x])
        x_array = scaler.transform(x1)
        prediction = model.predict(x_array)
        
        st.balloons()
        st.write(f"The Prediction is ${int(prediction)}")
        
        
    else:
        st.success("Please Enter Your Values for Prediction")
    
    
    
    
    
    

