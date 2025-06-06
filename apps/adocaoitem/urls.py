from django.urls import path, include
from rest_framework.routers import routers
from . import views

app_name = 'adocaoitem'
router = routers.DefaultRouter()
router.register('', views.adocaoitem, basename='adocaoitem')

urlpatterns = [
    path('', include(router.urls)),
]