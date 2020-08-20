# !pip install fastapi uvicorn

import uvicorn
from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()

with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

@app.get('/')
def index():
    return 'Use the /predict endpoint with a temperature argument'

@app.get('/predict')
def predict(temperature: float):
    new = pd.DataFrame({'temperature': [temperature]})
    prediction = pipe.predict(new)[0]
    return {'prediction': prediction}

if __name__ == '__main__':
    uvicorn.run(app)

# run at command line with:
# uvicorn app:app --port 5000 --reload