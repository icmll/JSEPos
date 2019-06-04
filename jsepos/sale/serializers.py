from rest_framework import serializers

from .models import Order
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    """serialize class Sale"""

    class Meta:
        model = Sale
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """serialize class Order"""

    class Meta:
        model = Order
        fields = '__all__'
