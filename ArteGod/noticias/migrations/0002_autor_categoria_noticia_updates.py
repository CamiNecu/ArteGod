import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs_and_resumen(apps, schema_editor):
    Noticia = apps.get_model("noticias", "Noticia")
    existing_slugs = set()

    for noticia in Noticia.objects.all().order_by("id"):
        base_slug = slugify(noticia.titulo) or f"noticia-{noticia.pk}"
        base_slug = base_slug[:50]
        candidate = base_slug
        suffix = 1
        while candidate in existing_slugs:
            suffix += 1
            candidate = f"{base_slug}-{suffix}"
            candidate = candidate[:80]
        existing_slugs.add(candidate)
        noticia.slug = candidate

        if not noticia.resumen and noticia.detalle:
            noticia.resumen = (noticia.detalle[:140] + "...") if len(noticia.detalle) > 140 else noticia.detalle

        if not noticia.publicado:
            noticia.publicado = noticia.created or django.utils.timezone.now()

        noticia.save(update_fields=["slug", "resumen", "publicado"])


def revert_slugs_and_resumen(apps, schema_editor):
    Noticia = apps.get_model("noticias", "Noticia")
    for noticia in Noticia.objects.all():
        noticia.slug = ""
        noticia.save(update_fields=["slug"])


class Migration(migrations.Migration):

    dependencies = [
        ("noticias", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=120, verbose_name="Nombre"),
                ),
                (
                    "cargo",
                    models.CharField(
                        blank=True, max_length=120, verbose_name="Cargo o rol"
                    ),
                ),
                (
                    "biografia",
                    models.TextField(blank=True, verbose_name="Biografía"),
                ),
                (
                    "correo",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="Correo de contacto"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado"),
                ),
            ],
            options={
                "verbose_name": "autor",
                "verbose_name_plural": "autores",
                "ordering": ("nombre",),
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=120, unique=True, verbose_name="Slug"),
                ),
                (
                    "descripcion",
                    models.TextField(blank=True, verbose_name="Descripción"),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True,
                        help_text="Clase CSS opcional para destacar la categoría",
                        max_length=20,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado"),
                ),
            ],
            options={
                "verbose_name": "categoría",
                "verbose_name_plural": "categorías",
                "ordering": ("nombre",),
            },
        ),
        migrations.AddField(
            model_name="noticia",
            name="autor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="noticias",
                to="noticias.autor",
                verbose_name="Autor",
            ),
        ),
        migrations.AddField(
            model_name="noticia",
            name="categoria",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="noticias",
                to="noticias.categoria",
                verbose_name="Categoría",
            ),
        ),
        migrations.AddField(
            model_name="noticia",
            name="es_destacada",
            field=models.BooleanField(default=False, verbose_name="Destacada"),
        ),
        migrations.AddField(
            model_name="noticia",
            name="publicado",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Publicado el"
            ),
        ),
        migrations.AddField(
            model_name="noticia",
            name="resumen",
            field=models.CharField(blank=True, max_length=255, verbose_name="Resumen"),
        ),
        migrations.AddField(
            model_name="noticia",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=180,
                verbose_name="Slug",
            ),
        ),
        migrations.AlterField(
            model_name="noticia",
            name="detalle",
            field=models.TextField(verbose_name="Contenido"),
        ),
        migrations.AlterField(
            model_name="noticia",
            name="imagen",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="noticias",
                verbose_name="Imagen",
            ),
        ),
        migrations.AlterField(
            model_name="noticia",
            name="titulo",
            field=models.CharField(max_length=150, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="noticia",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
        ),
        migrations.AlterField(
            model_name="noticia",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Actualizado"),
        ),
        migrations.RunPython(
            populate_slugs_and_resumen, revert_slugs_and_resumen
        ),
        migrations.AlterField(
            model_name="noticia",
            name="slug",
            field=models.SlugField(
                blank=True,
                max_length=180,
                unique=True,
                verbose_name="Slug",
            ),
        ),
    ]
