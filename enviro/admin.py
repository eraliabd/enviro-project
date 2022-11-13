from django.contrib import admin
from django.apps import apps

from .models import Main, Product, ProductCategory, WhyUs, Contact, Logo, Media

for model in apps.get_app_config('enviro').models.values():
    admin.site.register(model)
