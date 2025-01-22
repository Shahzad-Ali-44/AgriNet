from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model_path = "vgg19_model.keras"


try:
    MODEL = tf.keras.models.load_model(model_path)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    MODEL = None


CLASS_NAMES = [
    "Corn___Common_Rust", 
    "Corn___Gray_Leaf_Spot", 
    "Corn___Healthy", 
    "Corn___Northern_Leaf_Blight", 
    "Corn___Northern_Leaf_Spot", 
    "Corn___Phaeosphaeria_Leaf_Spot"
]


DISEASE_DETAILS = {
    "Corn___Common_Rust": {
        "symptoms": "Small, rust-colored spots on the leaves. These spots might be surrounded by yellowish areas.",
        "treatment": "Plant rust-resistant corn varieties and spray fungicides like Propiconazole or Mancozeb early."
    },
    "Corn___Gray_Leaf_Spot": {
        "symptoms": "Long gray or tan patches on the leaves that reduce the plant's ability to absorb sunlight.",
        "treatment": "Make sure plants have good airflow by reducing density, and spray fungicides such as Azoxystrobin."
    },
    "Corn___Healthy": {
        "symptoms": "Leaves look green, fresh, and healthy with no signs of disease.",
        "treatment": "No treatment needed. Keep watering regularly and provide proper nutrients to maintain health."
    },
    "Corn___Northern_Leaf_Blight": {
        "symptoms": "Long, cigar-shaped tan patches on the leaves that might feel slightly sunken.",
        "treatment": "Spray fungicides like Pyraclostrobin and rotate crops to keep the disease from coming back."
    },
    "Corn___Northern_Leaf_Spot": {
        "symptoms": "Small, round or oval spots on the leaves that turn brown or gray over time.",
        "treatment": "Use resistant corn varieties and spray fungicides on the leaves as needed."
    },
    "Corn___Phaeosphaeria_Leaf_Spot": {
        "symptoms": "Tiny, wet-looking spots on leaves that grow into long, brown streaks.",
        "treatment": "Choose resistant corn varieties and clean up any infected plant parts in the field."
    }
}



def read_file_as_image(data) -> np.ndarray:
    try:
        image = Image.open(BytesIO(data)).convert("RGB")
        image = image.resize((224, 224))  
        image_array = np.array(image) / 255.0  
        logging.debug(f"Image shape after preprocessing: {image_array.shape}")
        return image_array
    except Exception as e:
        logging.error(f"Error reading image file: {e}")
        raise ValueError("Invalid image data.")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if MODEL is None:
        return {"error": "Model is not loaded properly."}

    try:
        image_data = await file.read()
        image = read_file_as_image(image_data)
        img_batch = np.expand_dims(image, axis=0)  

        logging.debug(f"Image batch shape: {img_batch.shape}")

       
        predictions = MODEL.predict(img_batch)
        logging.debug(f"Predictions: {predictions}")

        predicted_class_idx = np.argmax(predictions[0])
        predicted_class = CLASS_NAMES[predicted_class_idx]
        confidence = float(np.max(predictions[0]))

       
        disease_details = DISEASE_DETAILS.get(predicted_class, {})


        logging.debug(f"Predicted class index: {predicted_class_idx}")
        logging.debug(f"Predicted class name: {predicted_class}")



        return {
            'class': predicted_class,
            'confidence': confidence,
            'symptoms': disease_details.get("symptoms", "No symptoms available."),
            'treatment': disease_details.get("treatment", "No treatment information available.")
        }

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return {"error": "An error occurred while processing the image."}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
