from django.urls import path, re_path

from .views import *

app_name = 'game'

urlpatterns = [
    path('merchant/', merchant, name='order_page'),
    path('warehouse/', warehouse_append, name='warehouse'),
    path('shop/', shop, name='shop')
]
