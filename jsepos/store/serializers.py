
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """serialize class User"""

    class Meta:
        model = User
        fields = '__all__'
