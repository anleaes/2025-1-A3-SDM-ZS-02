from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'adotante'

router = routers.DefaultRouter()
router.register('', views.AdotanteViewSet, basename='adotante')

urlpatterns = [
    path('', include(router.urls)),
]