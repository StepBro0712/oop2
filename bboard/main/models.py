from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Согласие на обработку персональных данных')

    class Meta(AbstractUser.Meta):
        pass


user_registrated = Signal(providing_args=['instance'])


class Order:
    pass