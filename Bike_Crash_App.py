#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

# Load the trained pipeline with SMOTE
#pipeline = joblib.load("C:/Users/Zeeshan/Downloads/Bike-Severity-Application-main/Bike-Severity-Application-main/random_forest_with_smote.joblib")
pipeline = joblib.load("random_forest_with_smote.joblib")

#pipeline = joblib.load("C:/Users/Zeeshan/Desktop/Python Codes/App/New folder (2)/random_forest_model.joblib")



st.title('Crash Severity Prediction App')

# Sidebar for user inputs
with st.sidebar:
    #st.header('User Inputs')
    st.header('Please Provide Input Selection to Predict the risk of getting into the Incident')
    day_of_week = st.selectbox('Day of Week', options=[('Monday', 0), ('Tuesday', 1), ('Wednesday', 2), ('Thursday', 3), ('Friday', 4), ('Saturday', 5), ('Sunday', 6)], format_func=lambda x: x[0])[1]
    active_school_zone_flag = st.selectbox('Active School Zone Flag', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])[1]
    speed_category = st.selectbox('Speed Category', options=[('Stop/Slow', 0), ('Medium', 1), ('High', 2)], format_func=lambda x: x[0])[1]
    crash_time_category = st.selectbox('Crash Time Category', options=[('Morning Rush Hour', 0), ('Afternoon Rush Hour', 1), ('Evening', 2), ('Late Night to Early Morning', 3), ('Unknown', 4)], format_func=lambda x: x[0])[1]
    surface_condition = st.selectbox('Surface Condition', options=[('Dry', 0), ('Wet', 1), ('Snow', 2), ('Ice', 3), ('Sand', 4), ('Water (Standing/Moving)', 5), ('Oil', 6), ('Other', 7)], format_func=lambda x: x[0])[1]
    person_helmet = st.selectbox('Person Helmet', options=[('Helmet Used', 0), ('Helmet Not Used', 1), ('No Helmet', 2), ('Not Applicable', 3), ('Unknown', 4)], format_func=lambda x: x[0])[1]
    intersection_related = st.selectbox('Intersection Related', options=[('Intersection', 0), ('Non-Intersection', 1), ('Intersection Related', 2), ('Driveway Access', 3), ('Unknown', 4)], format_func=lambda x: x[0])[1]
    construction_zone_flag = st.selectbox('Construction Zone Flag', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])[1]
    roadway_part = st.selectbox('Roadway Part', options=[('Main Lane', 0), ('Service/Frontage Road', 1), ('Exit/Entrance Ramp', 2), ('Non-Trafficway Area', 3)], format_func=lambda x: x[0])[1]
    traffic_control_type = st.selectbox('Traffic Control Type', options=[('No Control', 0), ('Stop Sign', 1), ('Yield Sign', 2), ('Flagman', 3), ('No Passing Zone', 4), ('School Zone', 5), ('Officer/Guard', 6), ('Flashing Light', 7), ('Signal Light', 8), ('Warning Sign', 9), ('Railroad Crossbuck', 10), ('Railroad Flashing Light', 11), ('Railroad Gates', 12), ('Other', 13), ('Unknown', 14)], format_func=lambda x: x[0])[1]
    
    #crash_year = st.selectbox('Crash Year', options=list(range(2010, 2018)))





    
    
    
    
    # Prepare user inputs for prediction
if st.button('Predict Severity'):
    # Create a DataFrame from user inputs
    input_features = pd.DataFrame({
        'Day of Week': [day_of_week],
        'Active School Zone Flag': [active_school_zone_flag],
        'Speed Category':[speed_category],
        'Crash Time Category':[crash_time_category],
        'Surface Condition':[surface_condition],
        'Person Helmet':[person_helmet],
        'Intersection Related':[intersection_related],
        'Construction Zone Flag':[construction_zone_flag],
        'Roadway Part':[roadway_part],
        'Traffic Control Type':[traffic_control_type]
       # 'Crash Year':[crash_year]
    })
    prediction = pipeline.predict(input_features)
    
    severity = {0: 'Low', 1: 'Medium', 2: 'High'}[prediction[0]]

    # Displaying the prediction and change background color
   # risk = change_background(severity)
    # Displaying the prediction
    st.header(f'Predicted Severity Level: {severity}')
    #st.subheader(risk)

    
    
# Displaying additional information based on the prediction
if 'severity' in locals():
    if severity == 'Low':
        st.write('Chances to meet with an incident is less ')
        st.image('GREEN.png', caption='Low Severity Scenario')
        st.header('Always were Helmet and follow traffic rules. The option you chose are safe for biking')
        # Optionally display an image or additional info
    elif severity == 'Medium':
        st.write('Chances to meet with an incident is medium')
        st.image('YELLOW.png', caption='Medium Severity Scenario')
        st.header('Follow Traffic rules and remember SOMEONE is Waiting FOR YOU, BEcarefull, Better Late Than Never')
        # Optionally display an image or additional info
    else:  # Assuming severity == 'High'
        st.write('Chances to meet with an incident is High, Be carefull')
        st.image('RED.png', caption='High Severity Scenario')
        st.header('Follow Traffic rules and remember SOMEONE is Waiting FOR YOU, BEcarefull, Better Late Than Never')
        # Optionally display an image or additional info
        
        # Display contributing parameters after prediction
    st.markdown("### Contributing Parameters:")
    st.markdown(f"- **Day of Week**: {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day_of_week]}")
    #st.markdown(f"- **Active School Zone Flag**: {'Yes' if active_school_zone_flag == 1 else 'No'}")
    st.markdown(f"- **Crash Time Category**: {['Morning Rush Hour', 'Afternoon Rush Hour', 'Evening', 'Late Night to Early Morning', 'Unknown'][crash_time_category]}")
    st.markdown(f"- **Speed Category**: {['Stop/Slow', 'Medium', 'High'][speed_category]}")
    st.markdown(f"- **Surface Condition**: {['Dry', 'Wet', 'Snow', 'Ice', 'Sand', 'Water (Standing/Moving)', 'Oil', 'Other'][surface_condition]}")
    st.markdown(f"- **Person Helmet**: {['Helmet Used', 'Helmet Not Used', 'No Helmet', 'Not Applicable', 'Unknown'][person_helmet]}")

        
       


    
# Repeat for other parameters you want to include
# Repeat for other parameters you want to include
    # Include other parameters
