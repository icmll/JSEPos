from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import list_route

from .serializers import UserSerializer
from .models import User
from .filters import UserFilter

# Create your views here.


class UserViewSet(GenericViewSet):
    """class UserViewSet"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter

    @list_route(methods=['get'])
    def filter_list(self, request):
        queryset = self.get_queryset()

        filter_queryset = self.filter_queryset(queryset)
        page_queryset = self.paginate_queryset(filter_queryset)
        serializers_queryset = self.get_serializer(page_queryset, many=True)
        return self.get_paginated_response(serializers_queryset.data)
