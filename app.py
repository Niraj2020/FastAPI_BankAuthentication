# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:40:41 2023

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle

# 2. Create the app object
app=FastAPI()
pickle_in=open("classifier.pkl", "rb")
classifier=pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name_str):
    return {'Welcome to my first web application': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_BankNotes(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    
    prediction=classifier.predict([[variance, skewness, curtosis, entropy]])
    if(prediction[0]>0.5):
        prediction="False note"
    else:
        prediction="It's a Bank Note"
    return {
        'prediction': prediction
    }        
    
    # 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    unicorn.run(app, host='127.0.0.1', port=8000)
    
    #uvicorn app:app --reload