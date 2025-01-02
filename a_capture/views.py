from django.http import JsonResponse
from .models import CapturedFrame

def upload_frame(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        CapturedFrame.objects.create(image=image)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)
