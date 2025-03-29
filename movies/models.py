from django.db import models

class Pelicula(models.Model):
    # Opciones para el campo 'genero'
    GENERO_CHOICES = [
        ('ACC', 'Acción'),
        ('COM', 'Comedia'),
        ('DRA', 'Drama'),
        ('TER', 'Terror'),
        ('SCI', 'Ciencia Ficción'),
        ('ANI', 'Animación'),
        ('DOC', 'Documental'),
        ('OTR', 'Otro'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    año_lanzamiento = models.IntegerField(verbose_name="Año de Lanzamiento")
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES, verbose_name="Género")
    duracion = models.IntegerField(verbose_name="Duración (minutos)")
    director = models.CharField(max_length=255, verbose_name="Director")
    actores_principales = models.TextField(verbose_name="Actores Principales", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    portada = models.ImageField(upload_to='portadas/', verbose_name="Portada", blank=True, null=True)
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['-fecha_creacion']

