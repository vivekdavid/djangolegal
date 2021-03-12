from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^googlecf4ff5ae26fa3a0a.html/$', views.google, name='google'),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^call-me/$', views.callme, name='callme'),
    url(r'^sent/$', views.sent, name='sent'),
	url(r'^assault-lawyer/$', views.assault, name='assaultlawyer'),
	url(r'^theft-lawyer/$',views.theft, name='theftlawyer'),
	url(r'^legal-aid-criminal-lawyer/$', views.legalaid, name='legalaid')]