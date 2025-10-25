from rest_framework import viewsets, status
from rest_framework.response import Response

# Models
from ..models import Prediction

# Services - handles the business logic for creating predictions
from ..services.prediction  import PredictionService

# Serializers - converts Prediction instances to JSON for API responses
from ..serializers.Prediction import PredictionResultSerializer


class PredictionViewSet(viewsets.ViewSet):
    """
    ViewSet for handling creation of predictions (image upload endpoint).
    Endpoint: /predict/
    """
    
    def create(self, request):
        """
        Handles POST requests with an uploaded image to create a new prediction.
        """
        try:
            # Call the service to handle all business logic: validation, model prediction, DB record creation
            prediction_instance = PredictionService.create_prediction_from_upload(request.data)
            
            # Serialize the Prediction instance into JSON format for API response
            serializer = PredictionResultSerializer(prediction_instance)
            
            # Return serialized data with HTTP 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Catch exceptions raised by the service
            # DRF will automatically handle common exceptions (ValidationError, NotFound, etc.) and convert to proper 4xx responses
            raise e


class PredictionHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for retrieving prediction history (read-only).
    Endpoints:
    - GET /predictions/       (List all predictions)
    - GET /predictions/{id}/  (Retrieve single prediction)
    """
    # Query predictions with related image and disease, ordered by most recent first
    queryset = Prediction.objects.select_related('image', 'disease').all().order_by('-predicted_at')
    # Serializer converts Prediction objects to JSON
    serializer_class = PredictionResultSerializer
