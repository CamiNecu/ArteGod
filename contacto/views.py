from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactoForm


def formulario_contacto(request):
    formulario = ContactoForm(request.POST or None)

    if request.method == "POST":
        if formulario.is_valid():
            messages.success(
                request,
                "¡Gracias por escribirnos! Responderemos tu mensaje lo antes posible.",
            )
            return redirect(f"{reverse('contacto:formulario')}?enviado=1")
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
