from django.contrib import admin
from .models import Autor, Categoria, Noticia


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "correo")
    search_fields = ("nombre", "correo")
    ordering = ("nombre",)
    readonly_fields = ("created", "updated")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "slug", "created")
    search_fields = ("nombre",)
    prepopulated_fields = {"slug": ("nombre",)}
    list_filter = ("created",)
    readonly_fields = ("created", "updated")
    ordering = ("nombre",)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "autor",
        "publicado",
        "es_destacada",
    )
    list_display_links = ("titulo",)
    list_filter = ("categoria", "autor", "es_destacada", "publicado")
    search_fields = ("titulo", "resumen", "detalle")
    autocomplete_fields = ("autor", "categoria")
    prepopulated_fields = {"slug": ("titulo",)}
    readonly_fields = ("created", "updated")
    ordering = ("-publicado",)
    date_hierarchy = "publicado"
    list_per_page = 20
