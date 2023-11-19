from .views import CornerImageViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'api-corners-ai'

router = routers.DefaultRouter()
router.register(r'corner_ai', CornerImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
