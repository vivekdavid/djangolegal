
from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^charges/$', views.charges, name='charges'),
    url(r'^assualt-dropped/$', views.assault, name='assault'),
    url(r'^assault-win/$', views.assaultwin, name='assaultwin'),
    url(r'^fail-to-comply/$', views.failtocomply, name='failtocomply'),
    url(r'^impaired-driving-suspension/$', views.impaired, name='impaired'),
    url(r'^impared-driving-win/$', views.impairedwin, name ='impairedwin'),
    url(r'^mischief/$', views.mischief, name='mischief'),
    url(r'^theft-dropped/$',views.theft, name='theft'),
    url(r'^theft-win/$',views.theftwin, name='theftwin'),
    url(r'^uttering-threats/$', views.utteringthreats, name='utteringthreats'),

]
