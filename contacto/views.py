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
            destinatario = getattr(settings, "CONTACT_EMAIL_TO", None) or settings.EMAIL_HOST_USER
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
                    "Gracias por escribirnos. Enviamos tu mensaje al buz\u00f3n configurado en Mailtrap.",
                )
                return redirect(f"{reverse('contacto:formulario')}?enviado=1")
            except Exception:
                messages.error(
                    request,
                    "No pudimos enviar tu mensaje. Verifica la configuracion de Mailtrap e intenta de nuevo.",
                )
        else:
            messages.error(
                request,
                "Revisa la informacion ingresada, algunos datos necesitan tu atencion.",
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
