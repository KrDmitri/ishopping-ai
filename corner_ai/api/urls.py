from .views import CornerImageViewSet
from .views import process_image_view
from rest_framework import routers
from django.urls import path, include

app_name = 'api-corners-ai'

router = routers.DefaultRouter()
router.register(r'corner_ai', CornerImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('process-image/', process_image_view, name='process_image'),
]
