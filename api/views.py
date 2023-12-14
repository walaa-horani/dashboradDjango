from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Chemistry
from .serializers import StudentSerializer,ChemistrySerializer

class  StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# Create your views here.

class  StudentrViewSet(viewsets.ModelViewSet):
    queryset = Chemistry.objects.all()
    serializer_class = ChemistrySerializer

