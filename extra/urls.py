from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.login_request),
    url(r'^manage/', views.manage_request)
]