from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
	path('',views.index),
	path('contact/',views.contact,name='contact'),
	path('writes/',views.writes,name='writes'),
	path('branch/',views.branch,name='branch'),
	path('category/', views.category, name='category'),
	url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
]