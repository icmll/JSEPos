

from .models import User
from django_filters.filterset import FilterSet


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = '__all__'
