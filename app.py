# 1. Library imports
import uvicorn
from typing import List
# from models import Test,  TableBdd, Data
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import pymysql
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import pickle
import pandas as pd
from Model import IrisModel, IrisSpecies

# 2. Create the app object
app = FastAPI()
model = IrisModel()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, stranger, from GitHub actions IISELII'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.get('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }


# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
