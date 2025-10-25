# Django imports
from django.core.paginator import Paginator
from django.http import Http404

# Third-party imports (Django REST Framework)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Local application imports
from ..exceptions.BadRequestException import BadRequestException
from ..models import Disease
from ..serializers.disease import DiseaseSerializer
from ..utils.pagination import get_pagination_params



class DiseaseList(APIView):
    """
    GET /api/diseases/?page=<int>&size=<int>

    Query Parameters:
        - page (int, optional): Page number to retrieve. Default = 1
        - size (int, optional): Number of records per page. Default = 10
    
    Retrieves a paginated list of diseases.
    """
    def get(self, request):
        
        page, size = get_pagination_params(request)

        diseases = Disease.objects.all()
        paginator = Paginator(diseases, size)
        page_obj = paginator.get_page(page)

        serializer = DiseaseSerializer(page_obj, many=True)

        return Response({
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": size,
            "results": serializer.data
        })
    

class DiseaseDetail(APIView):
    """
    GET /api/diseases/<pk>/

    Retrieves details of a specific disease by its ID.

    Path Parameters:
        - pk (int, required): The primary key (ID) of the disease.

    Response:
        Returns a JSON object with all available fields for the disease.

    """
    def get(self, request, pk, format=None):
        try:
            disease = Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            raise Http404("Disease not found")

        serializer = DiseaseSerializer(disease)
        
        return Response(serializer.data)

