from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

from .models import Goods
from .serializers import GoodsSerializer


# Create your views here.


class GoodsViewSet(GenericViewSet):

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    @list_route(methods=['get'])
    def filter_list(self, request):

        return Response({})

    @detail_route(methods=['get'])
    def fetch_one_forbarcode(self, request, pk=None):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer_ = self.get_serializer(filter_queryset.first())
        return Response(serializer_.data)
