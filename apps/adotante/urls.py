from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'adotante'

router = routers.DefaultRouter()
router.register('', views.AdotanteViewSet, basename='adotante')

urlpatterns = [
    path('', include(router.urls)),
]