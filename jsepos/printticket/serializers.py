from .models import PrintOrder
from rest_framework import serializers


class PrintOrderSerializer(serializers.ModelSerializer):
    """serialize class PrintOrder"""

    class Meta:
        model = PrintOrder
        fields = '__all__'

