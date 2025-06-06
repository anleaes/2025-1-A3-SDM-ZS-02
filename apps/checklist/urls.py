from django.urls import path, include
from rest_framework import routers
from .views import ChecklistViewSet

app_name = 'checklist'
router = routers.DefaultRouter()
router.register('', ChecklistViewSet, basename='checklist')

urlpatterns = [
    path('', include(router.urls)),
]