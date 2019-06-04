"""sale  models"""

from django.db import models
from goods.models import Goods
from store.models import User

# Create your models here.


class Order(models.Model):
    """class Order，一次结账为一次订单"""

    objects = models.Manager()

    order_status = ((0, "付清"), (1, "挂单"))
    sales_person = models.ForeignKey(User,
                                     blank=True,
                                     null=True,
                                     related_name='order',
                                     on_delete=models.SET_NULL,
                                     db_constraint=False)
    total_order_price = models.FloatField()
    be_given = models.FloatField()
    give_change = models.FloatField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=order_status)
    paidOff_datetime = models.DateTimeField(auto_now_add=True)
    print_count = models.IntegerField()


class Sale(models.Model):
    """class Sale，以商品为单位记录销售，每个对象为每件商品买一次"""

    objects = models.Manager()

    order = models.ForeignKey(Order,
                              related_name='sale',
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              db_constraint=False)
    goods = models.ForeignKey(Goods, blank=True, null=True, on_delete=models.SET_NULL, db_constraint=False)
