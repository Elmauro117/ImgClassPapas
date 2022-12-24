# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 17:12:30 2022

@author: CLIENTE
"""

from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf


app = FastAPI()

MODEL = tf.keras.models.load_model("./potatoes.h5") ## Donde sea que tengas guardado el modelo

CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]

@app.get("/ping")
async def ping():
    return "Bienvenit al modelo predictor de enfermedades de papas"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image 

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dmis(image,0) ### Sends batches of images
    
    prediction = MODEL.predict(img_batch)
        
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return{
        "class":predicted_class,
        "confidence":float(confidence)}
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


