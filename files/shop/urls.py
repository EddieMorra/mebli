from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from .views import SearchResultsView

app_name = 'shop'



urlpatterns = [
    path('', views.base_view, name='ProductList'),
    path('search_results/', views.SearchResultsView, name='search_results'),
    # url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('a/', include('defcat.urls')),
    # path('admin_tools/', include('admin_tools.urls')),

    path('post/<int:id>/<str:slug>/', views.post_detail, name='post_detail'), 
    # path('create/', PostCreate.as_view(), name="post_create_url"),





    # ('activity/', include('actstream.urls')),

    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
