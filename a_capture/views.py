from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CapturedFrame

@csrf_exempt
def upload_frame(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        CapturedFrame.objects.create(image=image)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)
