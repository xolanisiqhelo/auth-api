from .models import Role
from rest_framework import serializers
from django.contrib.auth.models import User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role', 'referenceNumber']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    role = RoleSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id',)

    def create(self, validated_data):
        role_data = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Role.objects.create(user=user, **role_data)
        return user
