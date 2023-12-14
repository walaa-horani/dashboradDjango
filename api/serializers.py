from rest_framework import serializers
from .models import Student, Chemistry

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class ChemistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Chemistry
        fields = "__all__"        