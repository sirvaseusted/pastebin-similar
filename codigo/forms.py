from django.forms import *
from django import forms
from codigo.models import *


class FormularioCodigo(ModelForm):
    class Meta:
        model = Codigo
        fields = ['nombre', 'codigo', 'expiracion',]
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control form-control-sm',  'required':'true'}),
            'codigo': Textarea(attrs={'class':'textarea form-control', 'id':'content', 'required':'true', 'style':'width: 100%; height: 500px; font-size: 10px; line-height: 18px;'}),
            'expiracion': Select(attrs={'type':'select', 'class':'form-control form-control-sm', 'required':'true'}),
            }