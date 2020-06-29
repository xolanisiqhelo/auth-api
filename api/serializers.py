from rest_framework import serializers
from .models import Role


class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
