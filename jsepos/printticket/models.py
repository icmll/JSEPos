from django.db import models
from sale.models import Order

# Create your models here.


class PrintOrder(models.Model):
    """class PrintOrder，以订单为单位，每打印一次为一个对象"""

    objects = models.Manager()

    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL, db_constraint=False)
    print_datetime = models.DateTimeField(auto_now_add=True)
