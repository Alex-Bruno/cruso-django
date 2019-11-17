from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    readonly_fields = ('visualizar_imagem',)
    raw_id_fields = ('autor', )
    date_hierarchy = 'publicado'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
    
    def visualizar_imagem(self,obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem Cadastrada" 
        
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'publicado')
    list_filter = ('nome', 'criado', 'publicado')
    search_fields = ('nome',)
    date_hierarchy = 'publicado'
    prepopulated_fields = {'slug': ('nome',)}
    
