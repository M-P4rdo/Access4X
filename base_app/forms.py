from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Administrador

class AdministradorForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ únicamente.')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Administrador
        fields = ('username', 'password','tipoDocumento', 'numDocumento','nombre','apellido','entidad', 'correo','superAdmin')

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        administrador = super(AdministradorForm, self).save(commit=False)
        administrador.user = user
        if commit:
            administrador.save()
        return administrador