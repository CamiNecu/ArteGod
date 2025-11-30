from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render

from noticias.models import Noticia
from .forms import RegistroBaseForm

EDITOR_GROUP = "Editores"
REPORTERO_GROUP = "Reporteros"

NOTICIA_PERMS_EDITOR = [
    "add_noticia",
    "change_noticia",
    "delete_noticia",
    "view_noticia",
]
NOTICIA_PERMS_REPORTERO = [
    "add_noticia",
    "view_noticia",
]


def ensure_group_with_perms(name: str, perm_codenames: list[str]):
    group, _ = Group.objects.get_or_create(name=name)
    content_type = ContentType.objects.get_for_model(Noticia)
    perms = Permission.objects.filter(codename__in=perm_codenames, content_type=content_type)
    group.permissions.add(*perms)
    return group


def _handle_registration(request, group_name: str, perm_codenames: list[str], rol_label: str):
    form = RegistroBaseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            codigo = form.cleaned_data.get("codigo_acceso")
            if codigo != settings.ACCOUNTS_INVITE_CODE:
                form.add_error("codigo_acceso", "Codigo de invitacion incorrecto.")
                return render(request, "accounts/registro.html", {"form": form, "rol": rol_label})
            user = form.save(commit=False)
            user.is_staff = True  # acceso al panel de administracion
            user.save()
            group = ensure_group_with_perms(group_name, perm_codenames)
            user.groups.add(group)
            messages.success(
                request,
                f"Usuario creado como {rol_label}. Ahora puedes iniciar sesion en el panel de administracion.",
            )
            return redirect("/admin/login/")
        messages.error(request, "Revisa los datos, hay campos con errores.")
    return render(request, "accounts/registro.html", {"form": form, "rol": rol_label})


def registro_editor(request):
    return _handle_registration(request, EDITOR_GROUP, NOTICIA_PERMS_EDITOR, "Editor")


def registro_reportero(request):
    return _handle_registration(request, REPORTERO_GROUP, NOTICIA_PERMS_REPORTERO, "Reportero")
