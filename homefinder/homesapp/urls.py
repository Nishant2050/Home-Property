from django.conf.urls import include, url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.LocationView.as_view(),name='property'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$',views.PropertyDetail.as_view(),name='propertyview'),
]
