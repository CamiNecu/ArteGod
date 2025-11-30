from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Field, HTML, Layout, Row


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre completo", max_length=120)
    correo = forms.EmailField(label="Correo electronico")
    motivo = forms.ChoiceField(
        label="Motivo de contacto",
        choices=(
            ("", "Selecciona una opcion"),
            ("consulta", "Consulta general"),
            ("obra", "Interes en una obra"),
            ("artista", "Colaboracion con artistas"),
            ("otro", "Otro"),
        ),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={"rows": 4}),
    )
    acepta_politica = forms.BooleanField(
        label="Acepto ser contactado por el equipo ArteGOD",
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "card card-body shadow-sm"
        self.helper.attrs = {"novalidate": "novalidate"}
        self.helper.layout = Layout(
            Row(
                Column("nombre", css_class="col-md-6 mb-3"),
                Column("correo", css_class="col-md-6 mb-3"),
            ),
            Row(
                Column("motivo", css_class="col-md-6 mb-3"),
                Column(Field("acepta_politica"), css_class="col-md-6 mb-3 d-flex align-items-end"),
            ),
            Div("mensaje", css_class="mb-3"),
            HTML(
                """
                <p class="small text-muted mt-3 mb-0">
                    Tu informacion se utiliza solo para responder a tu solicitud. No compartiremos tus datos con terceros.
                </p>
                """
            ),
        )
