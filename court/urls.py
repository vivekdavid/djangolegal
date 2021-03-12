from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^guide/$', views.toc, name='toc'),
    url(r'^what-to-expect/$', views.expect, name='expect'),
    url(r'^criminal-trials/$', views.fightthecharges, name='fightthecharges'),
    url(r'^evidence-dismissal/$', views.evidence, name = 'evidence'),
    url(r'^dismissal-for-delay/$', views.delay, name='delay'),

]
