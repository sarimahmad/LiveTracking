from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    username = models.CharField(max_length=232, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True,
                              error_messages={
                                  'null': 'This feild cannot be nulll'
                              })

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=13, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}"
