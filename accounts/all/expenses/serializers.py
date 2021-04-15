from rest_framework import serializers
from .models import *
from django_restql.mixins import DynamicFieldsMixin
from utils.utils import ModelValidationMixin


class AccountHeadSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = AccountHead 
        fields = '__all__'

class ExpenseSerializer(DynamicFieldsMixin, ModelValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Expense 
        fields = '__all__'