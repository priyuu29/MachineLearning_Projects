import streamlit as st
import joblib 
import pandas as pd
import numpy as np

#load model
model=joblib.load(r'C:\Users\priyu\OneDrive\Documents\ML\Project1\linear_regression_model.pkl')

#App Title

st.title("Aircraft Fuel Consumption Predictor")
# st.
#Input Field 
flight_Distance=st.number_input('Flight_Distance (km)')
number_of_Passenger=st.number_input('Number_of_Passenger')
flight_Duration=st.number_input('flight_duration (hours)')
aircraft_type=st.selectbox('Aircraft_Type',['Type1','Type2','Type3'])

#Dataframe

input_data=pd.DataFrame({
    'Flight_Distance':[flight_Distance],
    'Number_of_Passengers':[number_of_Passenger],
    'Flight_Duration':[flight_Duration],
    'Aircraft_Type_Type1':[1 if aircraft_type=='Type1' else 0],
    'Aircraft_Type_Type2':[1 if aircraft_type=='Type2' else 0],
    'Aircraft_Type_Type3':[1 if aircraft_type=='Type3' else 0],
})

#Prediction
if st.button('predict'):
    Fuel_Consumption=model.predict(input_data)
    st.write(Fuel_Consumption)