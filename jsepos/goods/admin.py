from django.contrib import admin

from .models import Goods
# Register your models here.


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    pass
