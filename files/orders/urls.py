from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate'),
    url(r'^admin/orders/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
    path('<str:order_id>/share/', views.OrderCreate, name='OrderCreate'), 
]