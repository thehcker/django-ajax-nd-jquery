from django.urls import path, include
from django.conf.urls import url
from book import views

urlpatterns = [
	path('', views.books_list, name = 'books_list'),
	path('base/', views.base, name = 'base'),
	url(r'^book/create/$', views.book_create, name='book_create'),
	url(r'^book/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
	url(r'^book/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete')


]