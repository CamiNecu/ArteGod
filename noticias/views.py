from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia

def Noticias(request):
    noticias_list = Noticia.objects.all()
    paginator = Paginator(noticias_list, 1)  # 1 noticias por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "noticias/noticias.html", {"page_obj": page_obj})