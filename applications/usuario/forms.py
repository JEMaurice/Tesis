from django import forms
from .models import Usuarios
from django.contrib.auth.hashers import make_password

""" LO QUE SE MUESTRA EN LA WEB, DANDOLE CLASES ATRIBUTOS O PROPIEDADES A LAS ETIQUETAS QUE UTILIZAMOS """


class FormUsuarios(forms.ModelForm):

    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "input-general"
            }
        )
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir Contraseña",
                "class": "input-general"
            }
        )
    )

    is_staff = forms.BooleanField(
        label="¿Es empleado autorizado?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox"
            }
        )
    )

    is_superuser = forms.BooleanField(
        label="¿Es encargado/administrador?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox"
            }
        )
    )

    usuario_activo = forms.BooleanField(
        label="¿Usuario activo?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox"
            }
        )
    )

    class Meta:
        model = Usuarios
        fields = (
            "username",
            "sector_asignado",
            "dni",
            "nombre",
            "apellido",
            "email",
            "direccion",
            "imagen",
            "telefono",
            "contacto",
            )
        widgets = {
            "imagen": forms.FileInput(attrs={'class':'form-control'}),
            "username": forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class": "input-general"}),
            "dni": forms.TextInput(attrs={"placeholder": "DNI", "class": "input-general"}),
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre completo", "class": "input-general"}),
            "apellido": forms.TextInput(attrs={"placeholder": "Apellidos", "class": "input-general"}),
            "email": forms.TextInput(attrs={"placeholder": "Correo electrónico", "class": "input-general"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Dirección", "class": "input-general"}),
            "telefono": forms.TextInput(attrs={"placeholder": "Teléfono", "class": "input-general"}),
            "contacto": forms.TextInput(attrs={"placeholder": "Número de contacto", "class": "input-general"}),
            "sector_asignado": forms.SelectMultiple(attrs={"class": "input-general"})
        }


class ModificarUserForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Contraseña",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña", 
                "class": "input-general"
            }
        )
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir Contraseña", 
                "class": "input-general"
            }
        )
    )

    is_staff = forms.BooleanField(
        label="¿Es personal autorizado?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox",
            }
        )
    )

    is_superuser = forms.BooleanField(
        label="¿Es superusuario?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox"
            }
        )
    )

    usuario_activo = forms.BooleanField(
        label="¿Usuario activo?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox"
            }
        )
    )

    class Meta:
        model = Usuarios
        fields = (
            "username",
            "sector_asignado",
            "dni",
            "nombre",
            "apellido",
            "email",
            "direccion"
            ,"imagen",
            "telefono",
            "contacto",
            )
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Nombre de usuario", "class": "input-general"}),
            "dni": forms.TextInput(attrs={"placeholder": "DNI", "class": "input-general"}),
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre completo", "class": "input-general"}),
            "apellido": forms.TextInput(attrs={"placeholder": "Apellidos", "class": "input-general"}),
            "email": forms.TextInput(attrs={"placeholder": "Correo electrónico", "class": "input-general"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Dirección", "class": "input-general"}),
            "telefono": forms.TextInput(attrs={"placeholder": "Teléfono", "class": "input-general"}),
            "contacto": forms.TextInput(attrs={"placeholder": "Número de contacto", "class": "input-general"}),
            "sector_asignado": forms.SelectMultiple(attrs={"class": "input-general"})
            }