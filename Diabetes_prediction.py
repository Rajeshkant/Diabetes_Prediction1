# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:26:28 2023

@author: jagad
"""

import numpy as np
import pickle
import streamlit as st

# loading Saved Model
loaded_model=pickle.load(open('C:/Users/jagad/Downloads/trained_model.sav','rb'))

#Prediction
def diabetes_prediction(input_data):
    # changing the input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    
    #Reshaping Input Data
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    # Giving Title
    st.title('Diabetes Prediction With Ml')
    
    #getting the Input data from enduser
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Value')
    BloodPressure = st.text_input('BloodPressure Value')
    SkinThickness = st.text_input('SkinThickness Value')
    Insulin = st.text_input('Insulin Value')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age of the Person')
    
    #code for Prediction
    diagnosis=""
    
    #Creating Examination for Prediction
    
    if st.button('Diabetes Test'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()