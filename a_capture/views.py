from rest_framework import viewsets
from rest_framework.response import Response
from .models import CapturedFrame
from .serializers import CapturedFrameSerializers
from rest_framework.parsers import MultiPartParser, FormParser

class CapturedFrameViewset(viewsets.ModelViewSet):
    queryset = CapturedFrame.objects.all()
    serializer_class = CapturedFrameSerializers
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        # Ensure that the request is in multipart form format
        if 'file' in request.FILES:
            file = request.FILES['file']
            # Handle the file and save it directly into the media field of the model
            captured_frame = CapturedFrame.objects.create(media=file)

            # Return the serialized data for the captured frame
            serializer = self.get_serializer(captured_frame)
            return Response(serializer.data, status=201)
        return Response({"error": "File not provided."}, status=400)
