from django.contrib import admin
from .models import Supplier, Ingredient

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Ingredient)