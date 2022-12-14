# Generated by Django 4.0.6 on 2022-10-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacto_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('asunto', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='panel_7c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('descripcion', models.TextField()),
                ('fondo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('informacion', models.TextField(blank=True)),
                ('creditos', models.CharField(max_length=300)),
                ('twitter', models.CharField(max_length=300)),
                ('linkedin', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('version', models.CharField(max_length=200)),
                ('ultima_actualizacion', models.CharField(max_length=200)),
                ('plataforma', models.CharField(max_length=200)),
                ('idioma', models.CharField(max_length=200)),
                ('tamanio', models.CharField(max_length=200)),
                ('licencia', models.CharField(max_length=200)),
                ('funcion1', models.TextField(blank=True)),
                ('funcion2', models.TextField(blank=True)),
                ('funcion3', models.TextField(blank=True)),
                ('funcion4', models.TextField(blank=True)),
                ('tecnologias', models.CharField(max_length=200)),
                ('tecnologias_icono', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link_descarga', models.CharField(max_length=400)),
                ('icono', models.FileField(blank=True, null=True, upload_to='images/')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
