from django import forms
from .models import Users

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['nombre', 'apellido', 'email', 'password']
