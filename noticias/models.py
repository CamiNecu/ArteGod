from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Autor(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre")
    cargo = models.CharField(
        max_length=120, blank=True, verbose_name="Cargo o rol"
    )
    biografia = models.TextField(blank=True, verbose_name="Biografía")
    correo = models.EmailField(blank=True, verbose_name="Correo de contacto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"
        ordering = ("nombre",)

    def __str__(self) -> str:
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    color = models.CharField(
        max_length=20,
        blank=True,
        help_text="Clase CSS opcional para destacar la categoría",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ("nombre",)

    def __str__(self) -> str:
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Noticia(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    slug = models.SlugField(max_length=180, unique=True, blank=True, verbose_name="Slug")
    resumen = models.CharField(max_length=255, blank=True, verbose_name="Resumen")
    detalle = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(
        upload_to="noticias", verbose_name="Imagen", blank=True, null=True
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.SET_NULL,
        related_name="noticias",
        null=True,
        verbose_name="Autor",
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name="noticias",
        null=True,
        verbose_name="Categoría",
    )
    es_destacada = models.BooleanField(default=False, verbose_name="Destacada")
    publicado = models.DateTimeField(default=timezone.now, verbose_name="Publicado el")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ("-publicado", "-created")

    def __str__(self) -> str:
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)[:50]
            candidate = base_slug
            index = 1
            while Noticia.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base_slug}-{index}"
                index += 1
            self.slug = candidate
        if not self.resumen:
            self.resumen = (self.detalle[:140] + "...") if self.detalle else ""
        super().save(*args, **kwargs)
