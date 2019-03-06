from django.conf.urls import url
from .views import products

urlpatterns = [
    url(r'^$', products, name='index'),
    url(r'^category/(?P<pk>\d+)/$', products, name='category'),
]
