from rest_framework.serializers import ModelSerializer
from .models import Goods


class GoodsSerializer(ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'
