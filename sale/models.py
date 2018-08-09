
"""sale  models"""

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
    """自定义用户类"""

    USER_STATUS = ((0, "正常"), (1, "禁用"))
    # 述用户模型字段名的字符串，被用于作为唯一的识别符。字段必须是唯一的（比如，在它的定义里设置 unique=True）
    user_name = models.CharField(max_length=9, unique=True)
    chinese_name = models.CharField(max_length=15)
    email = models.EmailField()

    # password AbstractBaseUser 中已经有了...无需申明
    # password = models.CharField(max_length=25)
    # 是否可以登入admin
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    status = models.CharField(max_length=1, choices=USER_STATUS)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    USERNAME_FIELD = 'user_name'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s%s' % (self.user_name, self.chinese_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email

    def get_email(self):
        "Returns the short name for the user."
        return self.user_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Order(models.Model):
    """class Order，一次结账为一次订单"""

    objects = models.Manager()

    order_status = ((0, "付清"), (1, "挂单"))
    sales_person = models.ForeignKey(User, blank=True, null=True, related_name='order', on_delete=models.SET_NULL)
    total_order_price = models.FloatField()
    be_given = models.FloatField()
    give_change = models.FloatField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=order_status)
    paidOff_datetime = models.DateTimeField(auto_now_add=True)
    print_count = models.IntegerField()


class Commodity(models.Model):
    """class Commodity，所有商品的价格条码等信息"""

    objects = models.Manager()

    commodity_name = models.CharField(max_length=30)
    bar_code = models.BigIntegerField()
    price = models.FloatField()


class Sale(models.Model):
    """class Sale，以商品为单位记录销售，每个对象为每件商品买一次"""
    
    objects = models.Manager()

    order = models.ForeignKey(Order, related_name='sale', blank=True, null=True, on_delete=models.SET_NULL)
    commodity = models.ForeignKey(Commodity, blank=True, null=True, on_delete=models.SET_NULL)


class PrintOrder(models.Model):
    """class PrintOrder，以订单为单位，每打印一次为一个对象"""
    
    objects = models.Manager()

    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    print_datetime = models.DateTimeField(auto_now_add=True)
