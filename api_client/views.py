from django.conf import settings
from django.shortcuts import render

from .services import obtener_noticias_api


def noticias_api(request):
    endpoint = settings.API_NOTICIAS_ENDPOINT
    noticias = obtener_noticias_api(endpoint)
    error = noticias is None
    context = {
        "noticias_api": noticias or [],
        "endpoint": endpoint,
        "error": error,
        "total": len(noticias or []),
    }
    return render(request, "api_client/noticias_api.html", context)
