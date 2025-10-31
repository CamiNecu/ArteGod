from datetime import datetime

from noticias.models import Categoria


def site_context(request):
    categorias_destacadas = Categoria.objects.all()[:5]
    site_info = {
        "brand": "ArteGOD",
        "email": "artegod@gmail.com",
        "phone": "+56 8 000 42958",
        "address": "Autop. Concepción - Talcahuano 7421, Talcahuano, Bío Bío",
    }
    return {
        "site_info": site_info,
        "categorias_destacadas": categorias_destacadas,
        "current_year": datetime.now().year,
    }
