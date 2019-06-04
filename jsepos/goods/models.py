from django.db import models

# Create your models here.


class Goods(models.Model):
    """class Goods，所有商品的价格条码等信息"""

    objects = models.Manager()

    goods_name = models.CharField(max_length=30)
    bar_code = models.BigIntegerField()
    price = models.FloatField()
