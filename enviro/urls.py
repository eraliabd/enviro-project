from django.urls import path
from .views import index, product, media, building, building_data, contact

app_name = 'enviro'

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('media/', media, name='media'),
    path('building/', building, name='building'),
    path('building_data/', building_data, name='building_data'),
    path('contact/', contact, name='contact'),
]
