from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta
# from django.utils import timezone
# from django.utils.timezone import now
# datetime vs timezone


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    # uniq  link
    # active_key = models.CharField(max_length=128, verbose_name='код подтверждения', blank=True)
    # # srok xraneniya
    # active_key_expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(48))
    #
    # def is_active_key_expires(self):
    #     if now() <= self.active_key_expires:
    #         return False
    #     else:
    #         return True

    active_key = models.CharField(verbose_name='ключ подтверждения', max_length=128, blank=True)
    active_key_expires = models.DateTimeField(
        verbose_name='актуальность ключа',
        default=(now() + timedelta(hours=48)))

    def is_active_key_expired(self):
        if now() <= self.active_key_expires:
            return False
        else:
            return True

