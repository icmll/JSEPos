

from django_filters.filterset import FilterSet

from .models import Goods


class GoodsFilterSet(FilterSet):

    class Meta:
        model = Goods
        fields = '__all__'
