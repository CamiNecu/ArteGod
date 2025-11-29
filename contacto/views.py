from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactoForm


def formulario_contacto(request):
    formulario = ContactoForm(request.POST or None)

    if request.method == "POST":
        if formulario.is_valid():
            data = formulario.cleaned_data
            asunto = f"Contacto ArteGOD - {data.get('motivo') or 'Mensaje'}"
            cuerpo = (
                "Nuevo mensaje recibido desde ArteGOD\n\n"
                f"Nombre: {data['nombre']}\n"
                f"Correo: {data['correo']}\n"
                f"Motivo: {data['motivo']}\n"
                f"Acepta ser contactado: {'Si' if data['acepta_politica'] else 'No'}\n\n"
                f"Mensaje:\n{data['mensaje']}"
            )

            # Destinatario ficticio, Mailtrap lo capturará
            destinatario = "test@example.com"

            try:
                send_mail(
                    asunto,
                    cuerpo,
                    settings.DEFAULT_FROM_EMAIL,
                    [destinatario],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    "Gracias por escribirnos. Tu mensaje fue enviado al buzón de pruebas de Mailtrap.",
                )
                return redirect(f"{reverse('contacto:formulario')}?enviado=1")
            except Exception as e:
                messages.error(
                    request,
                    f"No pudimos enviar tu mensaje. Verifica la configuración de Mailtrap. Error: {str(e)}",
                )
        else:
            messages.error(
                request,
                "Revisa la información ingresada, algunos datos necesitan tu atención.",
            )

    if request.GET.get("enviado"):
        messages.info(request, "Puedes enviarnos otro mensaje si lo necesitas.")

    return render(
        request,
        "contacto/formulario.html",
        {
            "form": formulario,
        },
    )
