from django.contrib import admin
from .models import Cliente, Carro, Aluguel, Perfil

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Aluguel)
admin.site.register(Perfil)
