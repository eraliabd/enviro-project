from django.urls import path
from .views import index, product, media, building, building_data, contact, order, success, order_success

app_name = 'enviro'

urlpatterns = [
    path('', index, name='index'),
    path('products/', product, name='product'),
    path('media/', media, name='media'),
    path('products/category_id=<int:pk>/', building, name='building'),
    path('product/category_id=<int:category_id>/<int:pk>/', building_data, name='building_data'),
    path('contact/', contact, name='contact'),
    path('order/<int:category_id>/product_id=<int:pk>/name=<str:name>', order, name='order'),
    path('contact/success/', success, name='success'),
    path('order/success', order_success, name='order_success'),
]
