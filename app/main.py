from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your pre-trained sentiment analysis model
model = joblib.load('app/model/sentiment_model.pkl')

# FastAPI app
app = FastAPI()

# Define the request body
class TextData(BaseModel):
    text: str

# Prediction endpoint
@app.post("/predict/")
def predict_sentiment(data: TextData):
    # Preprocess the data and make a prediction
    text = data.text
    prediction = model.predict([text])  # Replace with your model's prediction method
    return {"prediction": prediction[0]}
