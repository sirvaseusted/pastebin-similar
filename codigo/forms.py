from django.forms import *
from django import forms
from codigo.models import *


class FormularioCodigo(ModelForm):
    class Meta:
        model = Codigo
        fields = ['nombre', 'codigo', 'expiracion',]
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control form-control-sm',  'required':'true'}),
            'codigo': Textarea(attrs={'class':'form-control', 'required':'true'}),
            'expiracion': Select(attrs={'type':'select', 'class':'form-control form-control-sm', 'required':'true'}),
            } 
