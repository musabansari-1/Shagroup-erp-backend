from rest_framework import serializers
from .models import *
from django_restql.mixins import DynamicFieldsMixin
from utils.utils import ModelValidationMixin

class SSLCSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = SSLC 
        fields = '__all__'


class PUCSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = PUC 
        fields = '__all__'

class TrainerSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Trainer 
        fields = '__all__'

class TrainerRoleSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = TrainerRole
        fields = '__all__'

class ProjectSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = '__all__'

class StudentProjectSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentProject 
        fields = '__all__'