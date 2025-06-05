from django.urls import path, include
from . import views
from rest_framework import Router

# Criação url para o app animal

app_name = 'animal'

router = routers.DefaultRouter()
router.register('', views.AnimalViewSet, basename='animal')

urlpatterns = [
    path('', include(router.urls)),
    ]