from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allproductsapi/$', views.productlistapi.as_view(), name='allproductsapi'),
    url(r'^allcustomersapi/$', views.customerlistapi.as_view(), name='allcustomersapi'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
