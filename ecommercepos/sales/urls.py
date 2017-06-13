from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views, views_account


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^productdetail/(?P<pk>\w+)/$', views.ProductDetailView.as_view(), name='ProductDetailView'),
    url(r'^allproductsapi/$', views.productlistapi.as_view(), name='allproductsapi'),
    url(r'^allcustomersapi/$', views.customerlistapi.as_view(), name='allcustomersapi'),
    url(r'^newproduct/$', views.newproduct, name='newproduct'),
    url(r'^allsalesapi/$', views.salelistapi.as_view(), name='allsalesapi'),
    url(r'^cookiestest/$', views.cookiesandsessions, name='cookieandsessions'),
    url(r'^sendemail/$', views.sendemail),
    url(r'^safearea/$', views.safearea),
    #------------------------ Accounts ---------------------------
    url(r'^login/$', views_account.login_page, name='login_page'),
    url(r'^login_process/$', views_account.login_process, name='login_process'),
    url(r'^logout/$', views_account.logout, name='logout'), 
    url(r'^newuserregister/$', views.new_user_creation, name='newuserregister'),

]

#urlpatterns = format_suffix_patterns(urlpatterns)

