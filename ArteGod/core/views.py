from django.shortcuts import render

from noticias.models import Noticia


def home(request):
    obras = [
        {
            "titulo": "La joven de la perla",
            "autor": "Johannes Vermeer",
            "imagen": "core/assets/img/JovenPerla.jpeg",
        },
        {
            "titulo": "Autorretrato de Vincent Van Gogh (1889)",
            "autor": "Vincent van Gogh",
            "imagen": "core/assets/img/VincentSelf1889.jpg",
        },
        {
            "titulo": "Der Kuss",
            "autor": "Gustav Klimt",
            "imagen": "core/assets/img/TheKiss.jpg",
        },
    ]
    noticias_destacadas = (
        Noticia.objects.filter(es_destacada=True)
        .select_related("categoria")
        .order_by("-publicado")[:3]
    )
    return render(
        request,
        "core/home.html",
        {
            "obras": obras,
            "noticias_destacadas": noticias_destacadas,
        },
    )


def quienes(request):
    return render(request, "core/quienes.html")


def preguntasfre(request):
    return render(request, "core/preguntasfre.html")


def galimagenes(request):
    return render(request, "core/galimagenes.html")


def custom_404(request, exception=None):
    return render(request, "core/404.html", status=404)
