import numpy as np
import onnxruntime as ort
from fastapi import FastAPI, HTTPException, File, UploadFile
import pandas as pd
import uvicorn

MODEL_PATH = "model/model.onnx"

app = FastAPI()
session = ort.InferenceSession(MODEL_PATH)



class InputProcessor:
    """
    [ADD] Add preprocessing code if needed
    """
    def __init__(self, session):
        self.session = session
        

    def preprocess(self, df):
        return df



@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Receives a CSV file containing feature data, runs inference using the ONNX model,
    and returns the prediction results.

    The CSV file should not contain a header row. Each row should represent a sample,
    and columns should match the expected feature order.

    Args:
        file (UploadFile): CSV file uploaded via multipart/form-data.

    Returns:
        dict: A dictionary with the key 'prediction' containing the model's output.
    
    Example response:
    {
        "prediction": [1]
    }
    [ADD] Add code to recieve CSV file (temp.csv.), load model and return prediction
    """
    
    return {"prediction": ['Wrong response. No prediction yet.']}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
