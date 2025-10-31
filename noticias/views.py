from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Autor, Categoria, Noticia


def Noticias(request):
    noticias_queryset = Noticia.objects.select_related("categoria", "autor")

    categoria_slug = request.GET.get("categoria", "").strip()
    autor_id = request.GET.get("autor", "").strip()

    if categoria_slug:
        noticias_queryset = noticias_queryset.filter(categoria__slug=categoria_slug)
    if autor_id:
        noticias_queryset = noticias_queryset.filter(autor__id=autor_id)

    paginator = Paginator(noticias_queryset, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    filter_params = request.GET.copy()
    if filter_params.get("page"):
        filter_params.pop("page")
    base_querystring = filter_params.urlencode()

    context = {
        "page_obj": page_obj,
        "categorias": Categoria.objects.all(),
        "autores": Autor.objects.all(),
        "categoria_seleccionada": categoria_slug,
        "autor_seleccionado": autor_id,
        "querystring": base_querystring,
        "total_filtradas": noticias_queryset.count(),
        "filtros_activos": bool(categoria_slug or autor_id),
    }
    return render(request, "noticias/noticias.html", context)
