import logging
from . import models
from . import filters
from . import serializers
from django.views import View
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

logger = logging.getLogger(__name__)


# Create your views here.
class TestView(View):
    "调用测试视图"

    def get(self, request, *args, **kwargs):
        logger.info('start')
        print("aa")

        return JsonResponse({"result": "test ok!"})


class SaleViewSet(GenericViewSet):
    """class SaleViewSet"""
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer

    @list_route(methods=['get'])
    def filter_list(self, request):
        queryset = self.get_queryset()
        serializer_ = self.get_serializer(queryset, many=True)
        print(serializer_.data)
        return Response(serializer_.data)
