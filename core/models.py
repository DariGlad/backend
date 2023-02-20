from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        related_name='employees',
        null=True,
        verbose_name='Компания'
    )

    def __str__(self):
        return self.username
