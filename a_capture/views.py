from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CapturedFrame
from .serializers import CapturedFrameSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class CapturedFrameUploadView(APIView):
    def get(self, request, format=None):
        # Retrieve all captured frames from the database
        captured_frames = CapturedFrame.objects.all()
        serializer = CapturedFrameSerializer(captured_frames, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('media')
        if not file:
            return Response({"error": "No file provided"}, status=400)

        # Save the file or process it
        with open(f"frame/abunaim/{file.name}", "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)

        return Response({"message": "File uploaded successfully"}, status=200)
