from django.urls import path
from .views import index, product, media, building, building_data, contact, order, success

app_name = 'enviro'

urlpatterns = [
    path('', index, name='index'),
    path('products/', product, name='product'),
    path('media/', media, name='media'),
    path('building/<int:pk>/', building, name='building'),
    path('building_data/<int:pk>/', building_data, name='building_data'),
    path('contact/', contact, name='contact'),
    path('order/<int:pk>/', order, name='order'),
    path('contact/success/', success, name='success'),
]
