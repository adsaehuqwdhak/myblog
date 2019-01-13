from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns=[
	path('',views.list,name='blog'),
	url(r'^(?P<id>[0-9]+)/$', views.post, name='post'),
	#url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
	path('category/',views.category,name='category'),
]