from rest_framework import serializers

from sale.models import Commodity
from sale.models import User
from sale.models import Order
from sale.models import PrintOrder
from sale.models import Sale

class UserSerializer(serializers.ModelSerializer):
    """serialize class User"""
    class Meta:
        model = User
        fields = '__all__'

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

class CommoditySerializer(serializers.ModelSerializer):
    """serialize class Commodity"""
    class Meta:
        model = Commodity
        fields = '__all__'

class PrintOrderSerializer(serializers.ModelSerializer):
    """serialize class PrintOrder"""
    class Meta:
        model = PrintOrder
        fields = '__all__'
        
