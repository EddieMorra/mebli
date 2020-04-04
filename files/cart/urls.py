from django.conf.urls import url
from . import views
from django.urls import path, include

app_name = 'cart'

urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    # url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    path('add/<product_id>/', views.CartAdd, name='CartAdd'), 
    url(r'^$', views.CartDetail, name='CartDetail'),
    
]