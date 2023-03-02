from django.contrib import admin
from .models import Prod, Manufacturer, Category

# Register your models here.
admin.site.register(Prod)
admin.site.register(Manufacturer)
admin.site.register(Category)
