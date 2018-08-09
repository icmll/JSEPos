
from django.db.models import QuerySet
from typing import Any, Union

from sale import models
from sale import filters
from sale import serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route



# Create your views here.
class UserViewSet(GenericViewSet):
    """class UserViewSet"""
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class = filters.UserFilter


    @list_route(methods=['get'])
    def filter_list(self, request):
        queryset = self.get_queryset()

        filter_queryset = self.filter_queryset(queryset)
        page_queryset = self.paginate_queryset(filter_queryset)
        serializers_queryset = self.get_serializer(page_queryset, many=True)
        return self.get_paginated_response(serializers_queryset.data)

class OrderViewSet(GenericViewSet):
    """class OrderViewSet"""
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class PrintOrderViewSet(GenericViewSet):
    """class PrintOrderViewSet"""
    queryset = models.PrintOrder.objects.all()
    serializer_class = serializers.PrintOrderSerializer


class SaleViewSet(GenericViewSet):
    """class SaleViewSet"""
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class CommodityViewSet(GenericViewSet):
    """class CommodityViewSet"""
    queryset = models.Commodity.objects.all()
    serializer_class = serializers.CommoditySerializer
