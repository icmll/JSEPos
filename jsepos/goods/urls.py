
from django.conf.urls import include
from django.urls import path

from rest_framework import routers
from .views import GoodsViewSet

router = routers.DefaultRouter()
router.register(r'goods', GoodsViewSet)

urlpatterns = [
    path(r'api/', include(router.urls))
]
