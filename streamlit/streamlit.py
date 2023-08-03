# Import the necessary libraries
import streamlit as st
import requests
import json

# Define the FastAPI server endpoint
FASTAPI_SERVER_ENDPOINT = 'https://selmodockerapp.azurewebsites.net/predict'

# Create the Streamlit form
st.title("Iris Species Predictor : SUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
sepal_length = st.number_input('Insert sepal length')
sepal_width = st.number_input('Insert sepal width')
petal_length = st.number_input('Insert petal length')
petal_width = st.number_input('Insert petal width')

if st.button('Predict Species'):
    payload = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    response = requests.post(FASTAPI_SERVER_ENDPOINT, json=payload)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        probability = response.json()['probability']
        st.write(f'The predicted species is {prediction} with probability {probability}')
    else:
        st.write(f'Some error occurred: {response.text}')
