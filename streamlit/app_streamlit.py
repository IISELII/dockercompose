# Import the necessary libraries
import streamlit as st
import requests
import json

import mysql.connector
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import time
import os
from datetime import date
from datetime import datetime


st.set_page_config(page_title="IRIS_PREDICTIONS", page_icon=":pencil2:", layout="wide")



# Define the FastAPI server endpoint
FASTAPI_SERVER_ENDPOINT = 'https://webappapidms.azurewebsites.net/predict'


# Define MySQL DB Connection
config = {
    'host': secrets.BDD_HOST,
    'user': secrets.BDD_USER,
    'password': secrets.BDD_PASSWORD,
    'database': 'iris'
}

# Establish a new connection
conn = mysql.connector.connect(**config)
cursor = conn.cursor()


# Create the Streamlit form
st.title("Iris Species Predictor : ")
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

    cursor.execute(
        "INSERT INTO data_table (sepal_length, sepal_width, petal_length, petal_width) VALUES (%s, %s, %s, %s)",
        (sepal_length, sepal_width, petal_length, petal_width))
    conn.commit()

    response = requests.post(FASTAPI_SERVER_ENDPOINT, json=payload)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        probability = response.json()['probability']

        current_date = date.today().strftime("%d/%m/%Y")
        type(current_date)

        cursor.execute(
            "INSERT INTO pred_table (pred, proba, date) VALUES (%s, %s, %s)",
            (prediction, probability, current_date)
        )
        conn.commit()


        # accuracy = accuracy_score(type, y_pred)
        # precision = precision_score(type, y_pred, average='macro')
        # recall = recall_score(type, y_pred, average='macro')
        # f1 = f1_score(type, y_pred, average='macro')

        # Store in metric_table
        # cursor.execute(
        #     "INSERT INTO metric_table (accuracy, precision, recall, f1) VALUES (?, ?, ?, ?)",
        #     accuracy, precision, recall, f1)
        # conn.commit()


        st.write(f'The predicted species is {prediction} with probability {probability}')
    else:
        st.write(f'Some error occurred: {response.text}')



cursor.close()
conn.close()
