from django.urls import path, include
from . import views
from rest_framework import routers
from .serializers import AbrigoSerializer

app_name = 'abrigo'
router = routers.DefaultRouter()
router.register('', views.AbrigoViewSet, basename='abrigo')
urlpatterns = [
    path('', include(router.urls)),
]