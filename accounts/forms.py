from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório, digite um e-mail válido")
    first_name = forms.CharField(required=True, help_text="Obrigatório, digite o seu nome")
    last_name = forms.CharField(required=True, help_text="Obrigatório, digite o seu sobrenome")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado, por favor urilize outro.')