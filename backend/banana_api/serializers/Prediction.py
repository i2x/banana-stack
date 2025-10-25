from rest_framework import serializers

# Import the models that the serializers will work with
from ..models import Prediction, ImageUpload, Disease


class ImageUploadSerializer(serializers.ModelSerializer):
    """
    Serializer for handling image file uploads.
    It takes an image file and saves it to an ImageUpload record.
    """

    image = serializers.ImageField(source='file_path')

    class Meta:
        model = ImageUpload
        fields = ['image']


class SimpleDiseaseSerializer(serializers.ModelSerializer):
    """
    A simplified serializer for the Disease model, used for nesting inside other serializers.
    This provides essential disease info without all the details.
    """
    class Meta:
        model = Disease
        fields = ['disease_id', 'name', 'description']


class PredictionResultSerializer(serializers.ModelSerializer):
    """
    Serializer to format the final prediction result that is sent back to the user.
    It combines data from the Prediction, Disease, and ImageUpload models.
    """
    # Use the simplified serializer to show nested disease information
    disease = SimpleDiseaseSerializer(read_only=True)
    
    # Use a SerializerMethodField to create a full, absolute URL for the image
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Prediction
        # Define the fields to include in the JSON output
        fields = [
            'prediction_id', 
            'disease', 
            'confidence', 
            'predicted_at', 
            'image_url'
        ]

    def get_image_url(self, obj):
        """
        Generates the full URL for the associated image.
        'obj' here is the Prediction instance.
        """
        request = self.context.get('request')
        # This now correctly accesses 'obj.image.file_path.url'
        if request and obj.image and hasattr(obj.image, 'file_path'):
            if obj.image.file_path:
                return request.build_absolute_uri(obj.image.file_path.url)
        return None