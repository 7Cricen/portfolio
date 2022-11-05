from django import forms
from .models import programa, panel_7c, contacto_model

class programa_form(forms.ModelForm):
  class Meta:
    model = programa
    # fields = ['titulo','subtitulo','descripcion','version', 'ultima_actualizacion', 'plataforma', 'idioma', 'tamanio', 'licencia', 'funciones', 'tecnologias', 'tecnologias_icono', 'link_descarga', 'icono', 'portada']
    fields = "__all__"
    labels = {
      'tamanio':'Tamaño',
      'funcion1':'Funcion Principal 1',
      'funcion2':'Funcion Principal 2',
      'funcion3':'Funcion Principal 3',
      'funcion4':'Funcion Principal 4'
    }
    widgets = {
      'titulo':forms.TextInput(attrs={'class':'form-control my-3'}),
      'subtitulo':forms.TextInput(attrs={'class':'form-control my-3'}),
      'descripcion':forms.Textarea(attrs={'class':'form-control my-3'}),
      'version':forms.TextInput(attrs={'class':'form-control my-3'}),
      'ultima_actualizacion':forms.TextInput(attrs={'class':'form-control my-3'}),
      'plataforma':forms.TextInput(attrs={'class':'form-control my-3'}),
      'idioma':forms.TextInput(attrs={'class':'form-control my-3'}),
      'tamanio':forms.TextInput(attrs={'class':'form-control my-3'}),
      'licencia':forms.TextInput(attrs={'class':'form-control my-3'}),
      'funcion1':forms.Textarea(attrs={'class':'form-control my-3'}),
      'funcion2':forms.Textarea(attrs={'class':'form-control my-3'}),
      'funcion3':forms.Textarea(attrs={'class':'form-control my-3'}),
      'funcion4':forms.Textarea(attrs={'class':'form-control my-3'}),
      'tecnologias':forms.TextInput(attrs={'class':'form-control my-3'}),
      'tecnologias_icono':forms.TextInput(attrs={'class':'form-control my-3'}),
      'link_descarga':forms.TextInput(attrs={'class':'form-control my-3'}),
      'icono':forms.TextInput(attrs={'class':'form-control my-3'}),
      'portada':forms.TextInput(attrs={'class':'form-control my-3'}),
      'galeria_1':forms.TextInput(attrs={'class':'form-control my-3'}),
      'galeria_2':forms.TextInput(attrs={'class':'form-control my-3'}),
      'galeria_3':forms.TextInput(attrs={'class':'form-control my-3'}),
      'galeria_4':forms.TextInput(attrs={'class':'form-control my-3'}),
      'galeria_5':forms.TextInput(attrs={'class':'form-control my-3'}),
      'galeria_6':forms.TextInput(attrs={'class':'form-control my-3'}),
    }


class panel_7c_form(forms.ModelForm):
  class Meta:
    model = panel_7c
    fields = "__all__"
    widgets = {
      'titulo':forms.TextInput(attrs={'class':'form-control my-3'}),
      'titulo_pestania':forms.TextInput(attrs={'class':'form-control my-3'}),
      'logo':forms.TextInput(attrs={'class':'form-control my-3'}),
      'icono':forms.TextInput(attrs={'class':'form-control my-3'}),
      'descripcion':forms.Textarea(attrs={'class':'form-control my-3'}),
      'fondo':forms.TextInput(attrs={'class':'form-control my-3'}),
      'informacion':forms.Textarea(attrs={'class':'form-control my-3'}),
      'creditos':forms.TextInput(attrs={'class':'form-control my-3'}),
      'twitter':forms.TextInput(attrs={'class':'form-control my-3'}),
      'linkedin':forms.TextInput(attrs={'class':'form-control my-3'}),
    }


class contacto_form(forms.ModelForm):
  class Meta:
    model = contacto_model
    fields = "__all__"
    widgets = {
      'nombre':forms.TextInput(attrs={'class':'form-control my-3'}),
      'email':forms.TextInput(attrs={'class':'form-control my-3'}),
      'asunto':forms.TextInput(attrs={'class':'form-control my-3'}),
      'mensaje':forms.Textarea(attrs={'class':'form-control my-3'}),
    }