from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CapturedFrame
from .serializers import CapturedFrameSerializer

class CapturedFrameUploadView(APIView):
    def get(self, request, format=None):
        # Retrieve all captured frames from the database
        captured_frames = CapturedFrame.objects.all()
        serializer = CapturedFrameSerializer(captured_frames, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, format=None):
        serializer = CapturedFrameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Image received"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
