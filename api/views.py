from rest_framework import generics, permissions

from noticias.models import Noticia
from .serializers import NoticiaSerializer


class NoticiaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Noticia.objects.select_related("categoria", "autor").order_by("-publicado")
    serializer_class = NoticiaSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_slug = self.request.query_params.get("categoria")
        autor_id = self.request.query_params.get("autor")
        if categoria_slug:
            queryset = queryset.filter(categoria__slug=categoria_slug)
        if autor_id:
            queryset = queryset.filter(autor__id=autor_id)
        return queryset
