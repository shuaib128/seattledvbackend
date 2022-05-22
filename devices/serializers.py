from unicodedata import category
from rest_framework import serializers
from .models import Device, Model, Problem, Category

# Model serilizer
class ModelSereileizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image'
        )
        model = Model


# Problems serilizer
class ProblemSereileizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name'
        )
        model = Problem


# Problems serilizer
class DeviceCategorySereileizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name'
        )
        model = Category


# Device serilizer
class DeviceSereileizer(serializers.ModelSerializer):
    models = ModelSereileizer(many=True)
    problems = ProblemSereileizer(many=True)
    category = DeviceCategorySereileizer()
    class Meta:
        fields = (
            'id',
            'name',
            'models',
            'problems',
            'category'
        )
        model = Device