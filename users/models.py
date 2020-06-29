from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="role")
    role = models.CharField(max_length=10)
