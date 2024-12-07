from django.contrib import admin
from .models import Promocao, Empresa, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Promocao)
admin.site.register(Empresa)