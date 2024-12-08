from django.contrib import admin
from django.urls import path, include
from promocoes.views import home  # Importa a função home
from django.conf.urls.static import static
from django.conf import settings
from promocoes.views import home, promofacil


urlpatterns = [
    path('', home, name = 'home'),
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('promocoes/', include('promocoes.urls')),
    path('promofacil/', promofacil, name='promofacil'),
]


if settings.DEBUG:  # Apenas durante o desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)