from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Store(models.Model):
    """商店"""

    objects = models.Manager()

    name = models.CharField(max_length=50)
    uuid = models.CharField(max_length=64)
    full_addr = models.CharField(max_length=50)
    mobile = models.IntegerField()
    sub_mobile = models.IntegerField()


class User(AbstractUser):
    """自定义用户类"""

    USER_STATUS = ((0, "正常"), (1, "禁用"))
    YES_OR_NO = ((0, "不是"), (1, "是"))
    # 述用户模型字段名的字符串，被用于作为唯一的识别符。字段必须是唯一的（比如，在它的定义里设置 unique=True）
    # user_name = models.CharField(max_length=9, unique=True)
    chinese_name = models.CharField(max_length=15)
    email = models.EmailField()

    # password AbstractBaseUser 中已经有了...无需申明
    # password = models.CharField(max_length=25)
    # 是否可以登入admin
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    status = models.CharField(max_length=1, choices=USER_STATUS, default=1)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL, db_constraint=False)
    is_store_admin = models.SmallIntegerField(choices=YES_OR_NO, default=0)

    # USERNAME_FIELD = 'user_name'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s%s' % (self.username, self.chinese_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email

    def get_email(self):
        "Returns the short name for the user."
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
