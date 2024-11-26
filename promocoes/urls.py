from django.urls import path
from . import views 

urlpatterns = [
	path('home/', views.home, name = 'home'),
	path('criar_produto/', views.criar_produto, name = 'criar_produto'),
	path('criar_empresa/', views.criar_empresa, name = 'criar_empresa')

]