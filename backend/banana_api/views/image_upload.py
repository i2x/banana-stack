from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.response import Response

from ..models import ImageUpload
from ..serializers.image import ImageSerializer
from ..utils.pagination import get_pagination_params

class ImageList(APIView):
    """
    GET /api/images/?page=<int>&size=<int>

    Query Parameters:
        - page (int, optional): Page number to retrieve. Default = 1
        - size (int, optional): Number of records per page. Default = 10
    
    Retrieves a paginated list of images.
    """
    def get(self, request): 
        page, size = get_pagination_params(request)
        
        ALLimage = ImageUpload.objects.all()
        paginator = Paginator(ALLimage, size)
        page_obj = paginator.get_page(page)

        serializer = ImageSerializer(page_obj, many=True)

        return JsonResponse({
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": page,
            "page_size": size,
            "results": serializer.data
        })

class ImageDetailView(APIView):
    """
    GET /api/images/<pk>/

    Path Parameters:
        - pk (int, required): The ID of the image to retrieve.
    
    Retrieves details of a specific image by ID.
    """
    def get(self, request, pk,):
        image_obj = get_object_or_404(ImageUpload, pk=pk)
        serializer = ImageSerializer(image_obj)
        return Response(serializer.data)