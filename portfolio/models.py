from django.db import models

# Create your models here.


class programa(models.Model):
  titulo = models.CharField(max_length=200)
  subtitulo = models.CharField(max_length=200)
  descripcion = models.TextField()
  version = models.CharField(max_length=200)
  ultima_actualizacion = models.CharField(max_length=200)
  plataforma = models.CharField(max_length=200)
  idioma = models.CharField(max_length=200)
  tamanio = models.CharField(max_length=200)
  licencia = models.CharField(max_length=200)
  funcion1 = models.TextField(blank=True)
  funcion2 = models.TextField(blank=True)
  funcion3 = models.TextField(blank=True)
  funcion4 = models.TextField(blank=True)
  tecnologias = models.CharField(max_length=200)
  tecnologias_icono = models.FileField(upload_to='images/', null=True, blank=True)
  link_descarga = models.CharField(max_length=400)
  icono = models.FileField(upload_to='images/', null=True, blank=True)
  portada = models.ImageField(upload_to='images/', null=True, blank=True)
  galeria_1 = models.ImageField(upload_to='images/', null=True, blank=True)
  galeria_2 = models.ImageField(upload_to='images/', null=True, blank=True)
  galeria_3 = models.ImageField(upload_to='images/', null=True, blank=True)
  galeria_4 = models.ImageField(upload_to='images/', null=True, blank=True)
  galeria_5 = models.ImageField(upload_to='images/', null=True, blank=True)
  galeria_6 = models.ImageField(upload_to='images/', null=True, blank=True)

  def __str__(self):
    return self.titulo


class panel_7c(models.Model):
  titulo = models.CharField(max_length=200)
  titulo_pestania = models.CharField(max_length=200, blank=True)
  logo = models.ImageField(upload_to='images/', null=True, blank=True)
  icono = models.FileField(upload_to='images/', null=True, blank=True)
  descripcion = models.TextField()
  fondo = models.ImageField(upload_to='images/', null=True, blank=True)
  informacion = models.TextField(blank=True)
  creditos = models.CharField(max_length=300)
  twitter = models.CharField(max_length=300)
  linkedin = models.CharField(max_length=300)


class contacto_model(models.Model):
  nombre = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  asunto = models.CharField(max_length=200)
  mensaje = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nombre