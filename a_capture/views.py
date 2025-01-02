from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CapturedFrame
from .serializers import CapturedFrameSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import os

class CapturedFrameUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        # Retrieve all captured frames from the database
        captured_frames = CapturedFrame.objects.all()
        serializer = CapturedFrameSerializer(captured_frames, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('media')
        if not file:
            return Response({"error": "No file provided"}, status=400)

        # Define the directory path where files should be saved
        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        frames_directory = os.path.join(project_directory, "frames")

        # Check if the directory exists, if not, create it
        if not os.path.exists(frames_directory):
            os.makedirs(frames_directory)

        # Save the file in the frames directory
        file_path = os.path.join(frames_directory, file.name)
        try:
            with open(file_path, "wb") as f:
                for chunk in file.chunks():
                    f.write(chunk)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

        return Response({"message": "File uploaded successfully"}, status=200)
