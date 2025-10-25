from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # เรียก exception handler ของ DRF ก่อน
    response = exception_handler(exc, context)

    if response is None:
        # Log error for debug
        logger.error(f"Unhandled exception: {exc}", exc_info=True)

        return Response({
            "status": "error",
            "message": str(exc),
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    if isinstance(response.data, dict):
        if "detail" in response.data:
            message = response.data["detail"]
        else:
            message = response.data
    else:
        message = str(response.data)

    response.data = {
        "status": "error",
        "message": message,
        "code": response.status_code
    }
    return response
