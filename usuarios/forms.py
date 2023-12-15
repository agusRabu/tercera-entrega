from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioAltaUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {'username': '', 'email': '', 'password1': '', 'password2': ''}

class FormularioEditarUsuario(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar Email', required=False)
    first_name = forms.CharField(label= 'Cambiar Nombre', required=False)
    last_name = forms.CharField(label= 'Cambiar Apellido', required=False)
    descripcion = forms.CharField(label= 'Descripción', required=False, widget=forms.Textarea)
    link = forms.URLField(label= 'Link', required=False)
    avatar = forms.ImageField(label='Avatar', required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'descripcion', 'link', 'avatar']
