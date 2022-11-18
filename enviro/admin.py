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


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Main)
admin.site.register(Product)
admin.site.register(Logo)
admin.site.register(WhyUs)
admin.site.register(Contact)
admin.site.register(Media)
admin.site.register(Order)
