# coding: utf-8

from django_filters import filters
from django_filters.filterset import FilterSet
from django.db.models import Q
from sale.models import Commodity
from sale.models import Order
from sale.models import PrintOrder
from sale.models import Sale
from sale.models import User


class UserFilter(FilterSet):
    
    class Meta:
        model = User
        fields = '__all__'


class OrderFilter(FilterSet):

    class Meta:
        model = Order
        fields = ['id', 'sales_person']


class CommodityFilter(FilterSet):
    
    class Meta:
        model = Commodity
        fields = ['id', 'commodity_name', 'bar_code']


class PrintOrderFilter(FilterSet):

    class Meta:
        model = PrintOrder
        fields = '__all__'


class SaleFilter(FilterSet):

    class Meta:
        model = Sale
        fields = ['order', 'commodity']
        # fields 设置要过滤的字段，默认就会生成过滤此字段的过滤器，loopup_expr='exact'
        # 以下也可重写此过滤器的过滤规则
        # 各字段的模糊搜索在view中设置，search_field = ('order', 'commodity')
        # 也可自定义查询字段  例： exam
        # exam = filters.MethodsFilter(methods="filter_exam"),
        # 就会在调用自定义的filter_exam函数过滤闯过来的exam字段（def filter_exam(self, queryset, name, value)）
        order = filters.NumberFilter(field_name='order__id')
        commodity = filters.CharFilter(field_name='commodity__commodity_name')



