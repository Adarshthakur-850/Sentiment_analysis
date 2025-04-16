from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("app/model/sentiment_model.pkl")

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(data: InputText):
    result = model.predict([data.text])
    return {"sentiment": result[0]}
