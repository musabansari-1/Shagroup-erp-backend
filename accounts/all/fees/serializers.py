from rest_framework import serializers
from .models import *
from django_restql.mixins import DynamicFieldsMixin
from utils.utils import ModelValidationMixin, IdInValidationMixin
from rest_framework.utils import  model_meta
from drf_writable_nested.serializers import WritableNestedModelSerializer
from administration.codelab_systems.student_projects.models import StudentProject 

class PaymentTypeSerializer(DynamicFieldsMixin, ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = PaymentType 
        fields = '__all__'

class CognitiveInternshipFeesSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    # mode_of_payment = PaymentTypeSerializer()

    class Meta(IdInValidationMixin.Meta):
        model = CognitiveInternshipFees 
        fields = '__all__'

    # def to_internal_value(self, data):
    #      self.fields['mode_of_payment'] = serializers.PrimaryKeyRelatedField(
    #          queryset=PaymentType.objects.all())
    #      return super(CognitiveInternshipFeesSerializer, self).to_internal_value(data) 
    # def create(self, validated_data):
        
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     if response.get('mode_of_payment', None):
    #         response['mode_of_payment'] = PaymentTypeSerializer(instance.mode_of_payment).data
    #     return response

class AcademicInternshipFeesSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    class Meta(IdInValidationMixin.Meta):
        model = AcademicInternshipFees 
        fields = '__all__'

class EmployeeInternshipFeesSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    class Meta(IdInValidationMixin.Meta):
        model = EmployeeInternshipFees 
        fields = '__all__'

class CognitiveWorkshopFeesSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    class Meta(IdInValidationMixin.Meta):
        model = CognitiveWorkshopFees 
        fields = '__all__'

class AcademicWorkshopFeesSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    class Meta(IdInValidationMixin.Meta):
        model = AcademicWorkshopFees
        fields = '__all__'

class StudentProjectFeesSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    class Meta(IdInValidationMixin.Meta):
        model = StudentProjectFees 
        fields = '__all__'

    balance = serializers.ReadOnlyField()

class StudentProjectFeesBalanceSerializer(DynamicFieldsMixin, IdInValidationMixin, serializers.ModelSerializer):
    class Meta(IdInValidationMixin.Meta):
        model = StudentProjectFees
        fields = ['student_id', 'name', 'register_no','contact_1', 'contact_2', 'actual_fees', 'paid_amount','balance']
    
    student_id = serializers.ReadOnlyField(source='received_from.id')
    name = serializers.ReadOnlyField(source='received_from.name')
    register_no = serializers.ReadOnlyField(source='received_from.register_no')
    actual_fees = serializers.ReadOnlyField(source='received_from.fees')
    contact_1 = serializers.ReadOnlyField(source='received_from.contact_1')
    contact_2 = serializers.ReadOnlyField(source='received_from.contact_2')



