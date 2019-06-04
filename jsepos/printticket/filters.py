

from django_filters.filterset import FilterSet

from .models import PrintOrder


class PrintOrderFilter(FilterSet):
    class Meta:
        model = PrintOrder
        fields = '__all__'
