from rest_framework import serializers

from noticias.models import Noticia


class NoticiaSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source="categoria.nombre", read_only=True)
    autor_nombre = serializers.CharField(source="autor.nombre", read_only=True)

    class Meta:
        model = Noticia
        fields = [
            "id",
            "titulo",
            "slug",
            "resumen",
            "detalle",
            "categoria",
            "categoria_nombre",
            "autor",
            "autor_nombre",
            "es_destacada",
            "publicado",
        ]
        read_only_fields = [
            "id",
            "slug",
            "publicado",
            "categoria_nombre",
            "autor_nombre",
        ]
