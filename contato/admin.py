from django.contrib import admin
from .models import Categoria, ContatoDj

# Register your models here.


class ContatoDjAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobreNome', 'telefone',
                    'email', 'data_criacao', 'categoria', 'exibir')
    list_display_links = ('id', 'nome', 'sobreNome')
    list_filter = ('categoria', )
    list_per_page = 5
    search_fields = ('nome', 'sobreNome', 'telefone')
    list_editable = ('telefone', 'exibir')


admin.site.register(Categoria)

admin.site.register(ContatoDj, ContatoDjAdmin)
