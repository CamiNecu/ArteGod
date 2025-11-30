from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroBaseForm(UserCreationForm):
    email = forms.EmailField(label="Correo", required=True)
    codigo_acceso = forms.CharField(
        label="Codigo de invitacion",
        help_text="Ingresa el codigo entregado a colaboradores.",
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "codigo_acceso",
            "password1",
            "password2",
        ]
        help_texts = {"username": None}
        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "password1": "Contrasena",
            "password2": "Confirmar contrasena",
            "codigo_acceso": "Codigo de invitacion",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"form-control {css}".strip()
