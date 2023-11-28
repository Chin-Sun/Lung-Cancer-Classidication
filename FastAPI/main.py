from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from PIL import Image
import numpy as np
from transformers import AutoImageProcessor, AutoModelForImageClassification
import os
import boto3
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

# AWS S3 credentials and bucket name
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = 'user-lung-images'

# Initialize AWS S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

# Load model directly
processor = AutoImageProcessor.from_pretrained("olp0qlo/lung-cancer-classification")
model = AutoModelForImageClassification.from_pretrained("olp0qlo/lung-cancer-classification")

# Define lung cancer types
lung_cancer_types = ['Adenocarcinoma', 'Large Cell Carcinoma', 'Squamous Cell Carcinoma', 'Normal lung']

@app.get("/")
async def read_root():
    return FileResponse("templates/index.html")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(content={"error": "No file part"}, status_code=400)

    try:
        s3.upload_fileobj(file.file, S3_BUCKET, file.filename)
        return JSONResponse(content={"message": "File uploaded successfully to S3"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/prediction")
async def prediction(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(content={"error": "No file part"}, status_code=400)

    try:
        img = Image.open(file.file)
        img = img.convert('RGB')
        img = img.resize((224, 224))  # Ensure the image size matches your model input
        img_array = np.array(img)
        img_array = img_array / 255.0  # Normalize pixel values

        # Reshape the image array to match the model's input shape
        img_array = np.expand_dims(img_array, axis=0)

        if predicted_class_index < len(lung_cancer_types):
            predicted_class = lung_cancer_types[predicted_class_index]
            print(predicted_class)
        else:
            predicted_class = 'Normal lung'
            print(predicted_class)

        return JSONResponse(content={"prediction": predicted_class})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
