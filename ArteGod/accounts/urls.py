from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("registro/editor/", views.registro_editor, name="registro_editor"),
    path("registro/reportero/", views.registro_reportero, name="registro_reportero"),
]
