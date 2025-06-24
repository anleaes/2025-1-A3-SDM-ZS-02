from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'adocaoitem'
router = routers.DefaultRouter()
router.register('', views.AdocaoItemViewSet, basename='adocaoitem')

urlpatterns = [
    path('', include(router.urls)),
]