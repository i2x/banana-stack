from django.urls import path
from .views.Prediction import PredictionViewSet, PredictionHistoryViewSet
from .views.disease import DiseaseList, DiseaseDetail
from .views.treatment import TreatmentList, TreatmentDetail
from .views.image_upload import ImageDetailView, ImageList
from .views.model_flie import ModelDetailView, ModelList

urlpatterns = [
    # Disease endpoints
    path(
        'diseases/', 
        DiseaseList.as_view(), 
        name='disease_list'
    ),
    path(
        'diseases/<int:pk>/', 
        DiseaseDetail.as_view(), 
        name='disease_detail'
    ),

    # Treatment endpoints
    path(
        'treatments/',
        TreatmentList.as_view(),
        name='treatment_list'
    ),
    path(
        'treatments/<int:pk>/', 
        TreatmentDetail.as_view(), 
        name='treatment-detail'
    ),
    
    # Image endpoints
    path(
        'images/',
        ImageList.as_view(), 
        name='image_list'
    ),
    path(
        'images/<int:pk>/', 
        ImageDetailView.as_view(), 
        name='image_detail'
    ),

    # Model endpoints
    path(
        'models/',
        ModelList.as_view(), 
        name='model_list'
    ),
    path(
        'models/<int:pk>/', 
        ModelDetailView.as_view(), 
        name='model_detail'
    ),

    # Predict endpoints
    path(
        'predict/', 
        PredictionViewSet.as_view({'post': 'create'}), 
        name='predict-create'
    ),
    path(
        'predictions/', 
        PredictionHistoryViewSet.as_view({'get': 'list'}), 
        name='prediction-history-list'
    ),
    path(
        'predictions/<int:pk>/', 
        PredictionHistoryViewSet.as_view({'get': 'retrieve'}), 
        name='prediction-history-detail'
    ),
]
