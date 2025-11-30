from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("quienes/", views.quienes, name="quienes"),
    path("preguntasfrecuentes/", views.preguntasfre, name="preguntas_frecuentes"),
    path("galeriaimagenes/", views.galimagenes, name="galeria_imagenes"),
]
