from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'tipo'

router = DefaultRouter()
router.register('', views.TipoViewSet, basename='tipo')

urlpatterns = [
    path('', include(router.urls)),
   
]