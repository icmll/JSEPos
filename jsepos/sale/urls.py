# -*- coding: utf-8 -*-

from django.conf.urls import include
from django.urls import path

from rest_framework import routers
from .views import SaleViewSet

router = routers.DefaultRouter()
router.register(r'sale', SaleViewSet)

urlpatterns = [
    path(r'api/', include(router.urls))
]
