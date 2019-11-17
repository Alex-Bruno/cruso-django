from ckeditor.widgets import CKEditorWidget
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Post
        fields = ('titulo', 'conteudo', 'categoria' ,'imagem', 'status')