from rest_framework import viewsets
from rest_framework.response import Response
from .models import CapturedFrame
from .serializers import CapturedFrameSerializers
from rest_framework.parsers import MultiPartParser, FormParser
import base64

class CapturedFrameViewset(viewsets.ModelViewSet):
    queryset = CapturedFrame.objects.all()
    serializer_class = CapturedFrameSerializers
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        try:
            if 'file' not in request.FILES:
                return Response({"error": "No file provided"}, status=400)
            
            file = request.FILES['file']
            if not file.content_type.startswith('image/'):
                return Response({"error": "Invalid file type"}, status=400)

            captured_frame = CapturedFrame.objects.create(media=file)
            serializer = self.get_serializer(captured_frame)
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)