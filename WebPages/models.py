from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self) :
        return (self.name)
