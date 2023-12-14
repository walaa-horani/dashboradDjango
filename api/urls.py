# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet,StudentrViewSet

router = DefaultRouter()
router.register('', StudentViewSet, basename='main')

urlpatterns = [
    path('', include(router.urls)),
]
