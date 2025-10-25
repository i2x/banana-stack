from rest_framework.views import APIView
from ..utils.pagination import get_pagination_params
from django.shortcuts import get_object_or_404
from ..models import ModelFile
from django.core.paginator import Paginator
from ..serializers.model_file import ModelFileSerializer
from django.http import JsonResponse
from rest_framework.response import Response

class ModelList(APIView):
    """
    GET /api/model/?page=<int>&size=<int>

    Query Parameters:
        - page (int, optional): Page number to retrieve. Default = 1
        - size (int, optional): Number of records per page. Default = 10
    
    Retrieves a paginated list of images.
    """
    def get(self, request): 
        page, size = get_pagination_params(request)
        
        ALLmodel = ModelFile.objects.all()
        paginator = Paginator(ALLmodel, size)
        page_obj = paginator.get_page(page)
        serializer = ModelFileSerializer(page_obj, many=True, context={"request": request})

        return JsonResponse({
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": size,
            "results": serializer.data
        })

class ModelDetailView(APIView):
    """
    GET /api/model/<pk>/

    Path Parameters:
        - pk (int, required): The ID of the image to retrieve.
    
    Retrieves details of a specific image by ID.
    """
    def get(self, request, pk,):
        image_obj = get_object_or_404(ModelFile, pk=pk)
        serializer = ModelFileSerializer(image_obj, context={"request": request})
        return Response(serializer.data)