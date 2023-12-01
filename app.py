import streamlit as st
import requests

'''
# Your TaxiFare Prediction
'''
st.markdown('''
Hi there. Let me make some predictions on your taxi fare, so you can think twice on whether you would like to take that taxi or maybe just walk.
''')

pickup_date = st.date_input("Date", value=None)
pickup_time = st.time_input("Time")
pickup_datetime = f"{pickup_date} {pickup_time}"
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, step=1)
if st.button('Predict Fare'):
    url = 'https://taxifare.lewagon.ai/predict'
    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()['fare']
        formatted_prediction = round(prediction, 2)
        st.success(f"The predicted fare amount is: {formatted_prediction}$")
    else:
        st.error("Prediction failed. Please check your inputs and try again.")
