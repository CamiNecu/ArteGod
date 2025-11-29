from django.urls import path

from . import views

app_name = "api_client"

urlpatterns = [
    path("", views.noticias_api, name="noticias_api"),
]
