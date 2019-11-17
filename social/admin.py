from django.contrib import admin
from .models import Link

# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('chave', 'criado', 'alterado')
    list_filter = ('chave', 'criado', 'alterado')
    search_fields = ('chave',)
    date_hierarchy = 'criado'
    readonly_fields = ('criado', 'alterado',)