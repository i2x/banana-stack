import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from django.conf import settings

class CnnModelHandler:
    """
    Singleton class to load and use the CNN model.
    Ensures the model is loaded only once to save resources.
    """
    _instance = None  # Stores the singleton instance
    model = None      # Stores the loaded CNN model
    class_names = None  # Stores class names for predictions

    # --- Model configuration ---
    # Path to the saved CNN model (.h5 file)
    MODEL_PATH = os.path.join(settings.BASE_DIR, 'banana_api', 'CnnModel', 'banana_cnn.h5')
    
    # Class names corresponding to the trained model
    CLASS_NAMES = [
        "Banana Black Sigatoka Disease",
        "Banana Bract Mosaic Virus Disease",
        "Banana Healthy Leaf",
        "Banana Insect Pest Disease",
        "Banana Moko Disease",
        "Banana Panama Disease",
        "Banana Yellow Sigatoka Disease"
    ]
    
    # Expected input image size (used during training)
    IMAGE_SIZE = (128, 128)

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of this class.
        - If no instance exists, create one and load the model.
        - Ensures the model is loaded only once when Django starts.
        """
        if cls._instance is None:
            cls._instance = cls()
            cls._instance.load_model()
        return cls._instance

    def load_model(self):
        """
        Loads the CNN model from the .h5 file.
        - Checks if the file exists.
        - Loads the model using tf.keras.models.load_model.
        - Sets class names for prediction.
        """
        if os.path.exists(self.MODEL_PATH):
            print(f"Loading model from: {self.MODEL_PATH}")
            self.model = tf.keras.models.load_model(self.MODEL_PATH)
            self.class_names = self.CLASS_NAMES
            print("Model loaded successfully.")
        else:
            raise FileNotFoundError(f"Model file not found at {self.MODEL_PATH}")

    def _preprocess_image(self, image_path):
        """
        Loads and preprocesses an image for CNN prediction:
        - Resize to IMAGE_SIZE
        - Convert to array
        - Normalize pixel values to [0, 1]
        - Expand dimensions to create a batch of size 1
        """
        img = image.load_img(image_path, target_size=self.IMAGE_SIZE)
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, image_path):
        """
        Predicts the class of an image using the CNN model:
        - Preprocesses the image
        - Passes it to the CNN model
        - Returns the predicted class name and confidence score
        """
        if self.model is None:
            raise RuntimeError("Model is not loaded.")
        
        processed_image = self._preprocess_image(image_path)
        
        # Perform prediction with the CNN model
        predictions = self.model.predict(processed_image, verbose=0)
        
        # Convert prediction results to class name and confidence
        score = float(np.max(predictions[0]))
        class_index = np.argmax(predictions[0])
        predicted_class = self.class_names[class_index]
        
        return predicted_class, score

# Pre-load the model handler instance when Django starts
# Allows immediate predictions without reloading the model
model_handler_instance = CnnModelHandler.get_instance()
