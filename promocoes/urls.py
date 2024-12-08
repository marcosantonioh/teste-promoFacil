from django.urls import path
from . import views 


urlpatterns = [
	path('', views.home, name = 'home'),
    path('promocoes/', views.home, name='promocoes'),
	path('criar_empresa/', views.criar_empresa, name = 'criar_empresa'),
    path('criar_promocao/', views.criar_promocao, name = 'criar_promocao')
]
