import os
from django.conf import settings
from rest_framework.exceptions import ValidationError, NotFound

# Models
from ..models import Disease, Prediction, ImageUpload

# Serializers - Note: Python convention is to use lowercase filenames (e.g., prediction.py)
from ..serializers.Prediction import ImageUploadSerializer

# Utils - Note: Python convention is to use lowercase filenames (e.g., cnn_model_handler.py)
from ..utils.Cnn_model_handler import model_handler_instance


class PredictionService:
    """
    Service class encapsulating the business logic for creating predictions.
    Handles image upload validation, model inference, and database record creation.
    """
    @staticmethod
    def create_prediction_from_upload(request_data):
        """
        Main logic for creating a prediction from an uploaded image:
        1. Validate and save uploaded image
        2. Run CNN model prediction
        3. Match predicted disease with the database
        4. Create a Prediction record linking image, disease, and confidence score
        """
        # Step 1: Validate the uploaded image using the serializer
        upload_serializer = ImageUploadSerializer(data=request_data)
        if not upload_serializer.is_valid():
            # Raise DRF ValidationError if the input data is invalid
            raise ValidationError(upload_serializer.errors)

        # Save the uploaded image instance in the database
        image_upload_instance = upload_serializer.save()

        # Get the full absolute path of the uploaded image
        # This path will be used by the CNN model for prediction
        image_path = image_upload_instance.file_path.path

        # Step 2: Predict disease using the CNN model handler
        try:
            predicted_disease_name, confidence = model_handler_instance.predict(image_path)
        except Exception as e:
            # Log the actual exception for debugging purposes
            print(f"ERROR: Model prediction failed - {e}")
            # Raise a general RuntimeError for the API response
            raise RuntimeError("An unexpected error occurred while processing the image.")

        # Step 3: Find the Disease object in the database matching the predicted name
        try:
            disease = Disease.objects.get(name=predicted_disease_name)
        except Disease.DoesNotExist:
            # Raise a 404 NotFound if the predicted disease does not exist in DB
            raise NotFound(detail=f"The predicted disease '{predicted_disease_name}' could not be found in the database.")

        # Step 4: Create and save a new Prediction record
        # Links the uploaded image, predicted disease, and confidence score
        prediction_instance = Prediction.objects.create(
            image=image_upload_instance,
            disease=disease,
            confidence=confidence
        )

        # Return the newly created Prediction instance
        return prediction_instance
