from django import forms
from .models import Sala

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class FormSala(forms.ModelForm):
    class Meta:
        model= Sala
        fields= (
            "name",
            "users",
            )
        widgets = {
            "name": forms.Select(attrs={"class": "input-general"}),
            "users": forms.SelectMultiple(attrs={"class": "input-general"}),
        }

    def __init__(self, *args, **kwargs):
        super(FormSala, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = self.fields['users'].queryset.exclude(id__in=[1, 2])
