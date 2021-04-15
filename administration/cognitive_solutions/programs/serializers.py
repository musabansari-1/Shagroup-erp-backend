from rest_framework import serializers
from .models import *
from drf_queryfields import QueryFieldsMixin
from django_restql.mixins import DynamicFieldsMixin
from utils.utils import ModelValidationMixin
from accounts.all.fees.serializers import CognitiveInternshipFeesSerializer


class CognitiveInternshipSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    # college = serializers.SlugRelatedField(slug_field='name', queryset= College.objects.all())
    # college = serializers.PrimaryKeyRelatedField(queryset= College.objects.all())
    # college = serializers.SerializerMethodField()
    # college_name = serializers.CharField(source='college.name', read_only=True)
    # college = CollegeSerializer()
    # ci_fees = CognitiveInternshipFeesSerializer(read_only=True, many=True)
    class Meta:
        model = CognitiveInternship
        fields = '__all__'

    # def get_college(self, obj):
    #     return obj.college.name
 

    # def validate(self, attrs):
    #     instance = CognitiveInternship(**attrs)
    #     instance.clean()
    #     return attrs

class AcademicInternshipSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = AcademicInternship
        fields = '__all__'


class EmployeeInternshipSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = EmployeeInternship
        fields = '__all__'


class CognitiveWorkshopSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = CognitiveWorkshop 
        fields = '__all__'


class AcademicWorkshopSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = AcademicWorkshop 
        fields = '__all__'


class CollegeSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = College 
        fields = '__all__'


class CompanySerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'

class CourseSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class FrontendSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Frontend 
        fields = '__all__'


class BackendSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Backend 
        fields = '__all__'


class InternshipSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Internship 
        fields = '__all__'

class BatchSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Batch 
        fields = '__all__'


class WorkshopSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Workshop 
        fields = '__all__'

class StreamSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Stream 
        fields = '__all__'