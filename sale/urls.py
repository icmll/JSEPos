# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from rest_framework import routers
from sale.views import UserViewSet
from sale.views import OrderViewSet
from sale.views import PrintOrderViewSet
from sale.views import CommodityViewSet
from sale.views import SaleViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'order', OrderViewSet)
router.register(r'print', PrintOrderViewSet)
router.register(r'sale', SaleViewSet)
router.register(r'commodity', CommodityViewSet)


urlpatterns = [
	url(r'^api/', include(router.urls))
]
