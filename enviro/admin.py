from django.contrib import admin
from django.apps import apps

from .models import Main, Product, ProductCategory, WhyUs, Contact, Logo, Media, Order


# for model in apps.get_app_config('enviro').models.values():
#     admin.site.register(model)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    # slug field
    # prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'product_category')
    list_filter = ('weight',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'product')
    list_filter = ('created',)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Main)
admin.site.register(Logo)
admin.site.register(WhyUs)
admin.site.register(Contact)
admin.site.register(Media)
