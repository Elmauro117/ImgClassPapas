# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 23:05:58 2022

@author: CLIENTE
"""

from google.cloud import storage
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
import requests
import response

model = None
interpreter = None
input_index = None
output_index = None

BUCKET_NAME = "tf-model-mauro-gcp" ### El nombre de buckt (tipo s3 de google)

CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]

def download_blob(bucket_name,source_blob_name,destination_file_name):
    storage_cliente = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)    

def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/Papasmodelo1_2.h5",   ## donde hayas subido tu model en GCP
            "/tmp/Papasmodelo1_2.h5",
            )
        model = tf.keras.models.load_model("/tmp/Papasmodelo1_2.h5")
    
    image  = request.files["file"]
    
    image = np.array(
        Image.open(image).convert("RGB").resize((256,256))
        )
    
    image = image/255 
    
    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)
    
    print("prediccion: ",predictions)
    
    predicted_class =  class_names[np.argmax(predictions[0])]
    confidence = round(100*(np.max(predictions[0])),2)
    
    return {"class ":predicted_class, "confidence ":confidence}
    
    
    
    
    
    
    
    
    
    