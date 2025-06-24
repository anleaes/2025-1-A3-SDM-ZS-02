from django .urls import path, include
from rest_framework import routers
from . import views

app_name = 'adocao'
router = routers.DefaultRouter()
router.register('', views.AdocaoViewSet, basename='adocao')

urlpatterns = [
    path('', include(router.urls)),
]