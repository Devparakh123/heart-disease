from tkinter import BitmapImage
import pandas as pd
import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')
def user_input_features():
    BMI = st.sidebar.text_input("BMI", "type here")
    physical_health = st.sidebar.slider('Physical Health (days)', 0, 30, 15)
    mental_health = st.sidebar.slider('Mental Health (days)', 0, 30, 15)
    sleep_time = st.sidebar.slider('Sleep Time (hours)', 0, 24, 7)

    
    Smoking = st.sidebar.radio('Do you smoke?', ('Yes', 'No'))
    alcohol_drinking = st.sidebar.radio('Do you drink alcohol?', ('Yes', 'No'))
    stroke = st.sidebar.radio('Have you ever had a stroke?', ('Yes', 'No'))
    diff_walking = st.sidebar.radio('Do you have difficulty walking?', ('Yes', 'No'))
    physical_activity = st.sidebar.radio('Do you engage in physical activity?', ('Yes', 'No'))
    asthma = st.sidebar.radio('Do you have asthma?', ('Yes', 'No'))
    kidney_disease = st.sidebar.radio('Do you have kidney disease?', ('Yes', 'No'))
    skin_cancer = st.sidebar.radio('Do you have skin cancer?', ('Yes', 'No'))


    
    # Convert 'Yes' to 1 and 'No' to 0 in a single line each
    smoking_binary, alcohol_drinking_binary, stroke_binary, diff_walking_binary, \
    physical_activity_binary, asthma_binary, kidney_disease_binary, skin_cancer_binary = (
       
        1 if Smoking == 'Yes' else 0,
        1 if alcohol_drinking == 'Yes' else 0,
        1 if stroke == 'Yes' else 0,
        1 if diff_walking == 'Yes' else 0,
        1 if physical_activity == 'Yes' else 0,
        1 if asthma == 'Yes' else 0,
        1 if kidney_disease == 'Yes' else 0,
        1 if skin_cancer == 'Yes' else 0
    )
 
   age_categories = st.sidebar.selectbox('Age Category', ('35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'))
   races = st.sidebar.selectbox('Race', ('American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'))
   diabetics = st.sidebar.selectbox('Diabetic Status', ('No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'))
   general_health = st.sidebar.selectbox('General Health', ('Excellent', 'Fair', 'Good', 'Poor', 'Very good'))
       age_categories_bin = {
        'AgeCategory_35-39': 1 if age_categories == '35-39' else 0,
        'AgeCategory_40-44': 1 if age_categories == '40-44' else 0,
        'AgeCategory_45-49': 1 if age_categories == '45-49' else 0,
        'AgeCategory_50-54': 1 if age_categories == '50-54' else 0,
        'AgeCategory_55-59': 1 if age_categories == '55-59' else 0,
        'AgeCategory_60-64': 1 if age_categories == '60-64' else 0,
        'AgeCategory_65-69': 1 if age_categories == '65-69' else 0,
        'AgeCategory_70-74': 1 if age_categories == '70-74' else 0,
        'AgeCategory_75-79': 1 if age_categories == '75-79' else 0,
        'AgeCategory_80 or older': 1 if age_categories == '80 or older' else 0
    }
    
     races_bin = {
        'Race_American Indian/Alaskan Native': 1 if races == 'American Indian/Alaskan Native' else 0,
        'Race_Asian': 1 if races == 'Asian' else 0,
        'Race_Black': 1 if races == 'Black' else 0,
        'Race_Hispanic': 1 if races == 'Hispanic' else 0,
        'Race_Other': 1 if races == 'Other' else 0,
        'Race_White': 1 if races == 'White' else 0
    }
    
     diabetics_bin = {
        'Diabetic_No': 1 if diabetics == 'No' else 0,
        'Diabetic_No, borderline diabetes': 1 if diabetics == 'No, borderline diabetes' else 0,
        'Diabetic_Yes': 1 if diabetics == 'Yes' else 0,
        'Diabetic_Yes (during pregnancy)': 1 if diabetics == 'Yes (during pregnancy)' else 0
    }
    
     general_health_bin = {
        'GenHealth_Excellent': 1 if general_health == 'Excellent' else 0,
        'GenHealth_Fair': 1 if general_health == 'Fair' else 0,
        'GenHealth_Good': 1 if general_health == 'Good' else 0,
        'GenHealth_Poor': 1 if general_health == 'Poor' else 0,
        'GenHealth_Very good': 1 if general_health == 'Very good' else 0
    }



def main() :
     st.title("heart-disease")
     st.sidebar.header("User Input Parameters")
     html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit heart-disease  ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    input_array = input_df.values.reshape(1, -1
    input_df = user_input_features()
    prediction = model.predict(input_df)
    prediction_label = 'Yes' if prediction[0] == 1 else 'No'
    st.subheader('Prediction')
    st.write(f"Predicted Heart Disease: {prediction_label}")


if __name__=='__main__':
    main()
    
    