from django.contrib import admin
from .models import Device, Model, Category, Problem

# Register your models here.
admin.site.register(Device)
admin.site.register(Model)
admin.site.register(Category)
admin.site.register(Problem)