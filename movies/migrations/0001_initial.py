# Generated by Django 5.1.7 on 2025-03-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('año_lanzamiento', models.IntegerField(verbose_name='Año de Lanzamiento')),
                ('genero', models.CharField(choices=[('ACC', 'Acción'), ('COM', 'Comedia'), ('DRA', 'Drama'), ('TER', 'Terror'), ('SCI', 'Ciencia Ficción'), ('ANI', 'Animación'), ('DOC', 'Documental'), ('OTR', 'Otro')], max_length=3, verbose_name='Género')),
                ('duracion', models.IntegerField(verbose_name='Duración (minutos)')),
                ('director', models.CharField(max_length=255, verbose_name='Director')),
                ('actores_principales', models.TextField(blank=True, null=True, verbose_name='Actores Principales')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas/', verbose_name='Portada')),
                ('disponible', models.BooleanField(default=True, verbose_name='Disponible')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
