from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'department', 'role']
        read_only_fields = ['id', 'email', 'department', 'role']

    def get_department(self, obj):
        return obj.get_department_display()

    def get_role(self, obj):
        return obj.get_role_display()

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    department = serializers.ChoiceField(choices= User.DEPARTMENT_CHOICES)
    role = serializers.ChoiceField(choices = User.ROLE_CHOICES)

    