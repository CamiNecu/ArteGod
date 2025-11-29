from django.urls import path

from .views import NoticiaListCreateAPIView

app_name = "api"

urlpatterns = [
    path("noticias/", NoticiaListCreateAPIView.as_view(), name="noticia-list-create"),
]
