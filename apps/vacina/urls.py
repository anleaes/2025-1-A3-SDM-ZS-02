from django.urls import path, include
from rest_framework.routers import routers
from .views import VacinaViewSet

app = 'vacina'
router = routers.DefaultRouter()
router.register('', VacinaViewSet, basename='vacina')
urlpatterns = [
    path('', include(router.urls)),
]