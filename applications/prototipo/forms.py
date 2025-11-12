from django import forms
from .models import NombrePrototipo, Prototipo, Piezas, PiezaPrototipo

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class FormPiezas(forms.ModelForm):
    class Meta:
        model = Piezas
        fields = (
            "nombre",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui", "class": "input-general"})
            }



class FormPiezaPrototipo(forms.ModelForm):
    class Meta:
        model = PiezaPrototipo
        fields = (
            "nombreprototipo",
            "tipo_pieza",
            "piezas",
            "cantidad",
            "ancho",
            "alto",
            "metros",
            )
        widgets  = {
            "nombreprototipo": forms.Select(attrs={'class':'input-general'}),
            "tipo_pieza": forms.Select(attrs={'class':'input-general'}),
            "piezas": forms.Select(attrs={'class':'input-general'}),
            "cantidad": forms.NumberInput(attrs={"class": "input-general", "step": "1"}),
            "ancho": forms.NumberInput(attrs={"class": "input-general", "step": "0.01"}),
            "alto": forms.NumberInput(attrs={"class": "input-general", "step": "0.01"}), 
            "metros": forms.NumberInput(attrs={"class": "input-general", "step": "0.01"}),
        }
    def clean_cantidad (self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad <= 0:
            raise forms.ValidationError(" el numero debe ser mayor a 0")
        return cantidad
    
    def clean_ancho (self):
        ancho = self.cleaned_data["ancho"]
        if ancho < 0:
            raise forms.ValidationError(" el numero debe ser mayor a 0")
        return ancho
    
    def clean_alto (self):
        alto = self.cleaned_data["alto"]
        if alto < 0:
            raise forms.ValidationError(" el numero debe ser mayor a 0")
        return alto
    
    def clean_metros (self):
        metros = self.cleaned_data["metros"]
        if metros < 0:
            raise forms.ValidationError(" el numero debe ser mayor a 0")
        return metros




class FormNombrePrototipo(forms.ModelForm):
    class Meta:
        model = NombrePrototipo
        fields = (
            "nombre",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui", "class": "input-general"})
            }



class FormPrototipo(forms.ModelForm):
    class Meta:
        model = Prototipo
        fields = (
            "id",
            "nombre",
            "prototipo_armado",
            "imagen",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui nombre fantasia", "class": "input-general"}),
            "prototipo_armado": forms.SelectMultiple(attrs={"class": "input-general"}),
            "imagen": forms.FileInput(attrs={'class':'form-control'}),
            }
        

class FormupdatePrototipo(forms.ModelForm):
    class Meta:
        model = Prototipo
        fields = (
            "id",
            "nombre",
            "prototipo_armado",
            "imagen",
            )
        widgets  = {
            "nombre" : forms.TextInput(attrs={"placeholder" : "Ingresar aqui nombre fantasia", "class": "input-general"}),
            "prototipo_armado": forms.SelectMultiple(attrs={"class": "input-general"}),
            }