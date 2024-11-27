
from django.contrib import admin
from django.urls import path, include
from promocoes.views import home  # Importa a função home

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', home, name = 'home'),
    path('promocoes/', include('promocoes.urls')),
    path('auth/', include('usuarios.urls'))
]
