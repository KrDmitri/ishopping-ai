from rest_framework import viewsets
from .serializers import CornerImageSerializer
from ..models import CornerImage
from django.http import JsonResponse
from .utils import process_image

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



class CornerImageViewSet(viewsets.ModelViewSet):
    queryset = CornerImage.objects.all().order_by('-uploaded')
    serializer_class = CornerImageSerializer

@method_decorator(csrf_exempt, name='dispatch')
def process_image_view(request):
    if request.method == 'POST':
        image = request.FILES.get('picture')
        result = process_image(image)
        return JsonResponse({'product_name': result})