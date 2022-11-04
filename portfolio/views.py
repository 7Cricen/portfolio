from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import programa_form, panel_7c_form, contacto_form
from .models import programa, panel_7c, contacto_model
import requests

from django.conf import settings

# from .my_captcha import FormWithCaptcha

# Create your views here.

def home(request):
  try:
    lista = programa.objects.all()
    ver_configuracion = get_object_or_404(panel_7c, pk=1)
    return render(request, 'home.html',{'programas':lista, 'configuracion':ver_configuracion})
  except:
    configuracion = panel_7c(
      titulo = 'Titulo Ejemplo',
      logo = '',
      descripcion = 'Ejemplo de una descripcion',
      fondo = '',
      informacion = 'Ejemplo de informacion personal' ,
      creditos = '© 2022 - Cricen Developer - All rights reserved.',
      twitter = 'link_ejemplo',
      linkedin = 'link_ejemplo'
    )
    configuracion.save()
    ver_configuracion = get_object_or_404(panel_7c, pk=1)
    return render(request, 'home.html',{'programas':lista, 'configuracion':ver_configuracion})


def registro(request):
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  if request.method == 'GET':
    return render(request, 'panel_7c/registro.html',{'form':UserCreationForm,'configuracion':ver_configuracion}) 

  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        usuario.save()
        login(request, usuario)
        return redirect('logear')

      except Exception as e:
        print(e) 
        return render(request, 'panel_7c/registro.html',{'form':UserCreationForm, 'error':'Nombre ocupado.'}) 

    return render(request, 'panel_7c/registro.html',{'form':UserCreationForm,'configuracion':ver_configuracion, 'error':'Las contraseñas no coinciden.'}) 


@login_required
def deslogear(request):
  logout(request)
  return redirect('home')


def logear(request):
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  if request.method == "GET":
    return render(request, 'panel_7c/login.html',{'form':AuthenticationForm,'configuracion':ver_configuracion}) 

  else:
    usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    # return render(request, home)

    if usuario is None:
        return render(request, 'panel_7c/login.html',{'form':AuthenticationForm,'configuracion':ver_configuracion, 'error':'Nombre o contraseñas incorrecta.'}) 

    else:
      login(request, usuario)
      return redirect('home')


@login_required(login_url='home')
def add_programa(request):
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  if request.method == "GET":
    return render(request, 'panel_7c/add_programa.html', {'form':programa_form,'configuracion':ver_configuracion})

  else:
    try:
      formulario = programa_form(request.POST, request.FILES)
      if formulario.is_valid():
        formulario.save()
        return redirect('home')

    except Exception as e:
        return render(request, 'panel_7c/add_programa.html',{'form':programa_form,'configuracion':ver_configuracion, 'error':e}) 


@login_required
def lista_programas(request):
  lista = programa.objects.all()
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  return render(request, 'panel_7c/lista.html',{'form':lista,'configuracion':ver_configuracion})


@login_required
def ver_programa(request, p_id):
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  if request.method == 'GET':
    ver_prog = get_object_or_404(programa, pk=p_id)
    formulario = programa_form(instance=ver_prog)
    return render(request, 'panel_7c/view_programa.html',{'programa':ver_prog,'configuracion':ver_configuracion, 'form':formulario})

  else:
    try:
      ver_prog = get_object_or_404(programa, pk=p_id)
      formulario = programa_form(request.POST, request.FILES, instance=ver_prog)

      if formulario.is_valid():
        formulario.save()
        return render(request, 'panel_7c/view_programa.html',{'programa':ver_prog,'configuracion':ver_configuracion, 'form':formulario, 'exito':'Se guardo correctamente'})

      else:
        formulario = programa_form(instance=ver_prog)
        return render(request, 'panel_7c/view_programa.html',{'programa':ver_prog,'configuracion':ver_configuracion, 'form':formulario, 'error':'formulario invalido'})

    except Exception as e:
      return render(request, 'panel_7c/view_programa.html',{'programa':ver_prog,'configuracion':ver_configuracion, 'form':formulario, 'error':e})


@login_required
def eliminar_programa(request, p_id):
  lista = programa.objects.all()
  if request.method == 'POST':
    try:
      ver = get_object_or_404(programa, pk=p_id)
      ver.delete()
      return redirect('lista')
    except Exception as e:
      return render(request, 'panel_7c/lista.html',{'form':lista, 'error':e})
  else:
      return render(request, 'panel_7c/lista.html',{'form':lista, 'error':'Algo paso'})


def ver_project(request, p_id):
  ver = get_object_or_404(programa, pk=p_id)
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  return render(request, 'projects.html',{'programa':ver,'configuracion':ver_configuracion})


def contacto(request):
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  if request.method == 'GET':
    return render(request, 'contacto.html', {'configuracion':ver_configuracion,'form':contacto_form, 'site_key':settings.RECAPTCHA_SITE_KEY})
  else:
    
    secret_key = settings.RECAPTCHA_SECRET_KEY
    data = request.POST
    # captcha verification
    data = {
        'response': data.get('g-recaptcha-response'),
        'secret': secret_key
    }
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result_json = resp.json()

    print(result_json)

    if result_json.get('success'):
      # return render(request, 'contact_sent.html', {'is_robot': True})
    # end captcha verification
      nombre = request.POST['nombre']
      email = request.POST['email']
      asunto = request.POST['asunto']
      mensaje = request.POST['mensaje']
      c = contacto_model(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
      c.save()
      return render(request, 'contacto.html', {'configuracion':ver_configuracion, 'enviado':True, 'nombre':nombre})
    else:
      return render(request, 'contacto.html', {'configuracion':ver_configuracion, 'enviado':False, 'is_robot':True})
      


def panel_7c_v(request):
  if request.method == 'GET':
    try:
      ver_configuracion = get_object_or_404(panel_7c, pk=1)
      formulario = panel_7c_form(instance=ver_configuracion)
      return render(request, 'panel_7c/panel_7c.html',{'form':formulario,'configuracion':ver_configuracion})

    except Exception as e:
      return render(request, 'panel_7c/panel_7c.html',{'form':panel_7c_form, 'error':e})

  else:
    try:
      ver_configuracion = get_object_or_404(panel_7c, pk=1)
      formulario = panel_7c_form(request.POST, request.FILES, instance=ver_configuracion)
      if formulario.is_valid():
        formulario.save()
        return render(request, 'panel_7c/panel_7c.html',{'form':formulario,'configuracion':ver_configuracion, 'exito':'Se guardo correctamente'})
      else:
        return render(request, 'panel_7c/panel_7c.html',{'form':panel_7c_form,'configuracion':ver_configuracion, 'error':'Formulario invalido'})

    except:
      formulario = panel_7c_form(request.POST, request.FILES)
      if formulario.is_valid():
        formulario.save()
        return render(request, 'panel_7c/panel_7c.html',{'form':formulario,'configuracion':ver_configuracion, 'exito':'Se guardo correctamente'})
      else:
        return render(request, 'panel_7c/panel_7c.html',{'form':panel_7c_form,'configuracion':ver_configuracion, 'error':'Formulario invalido'})

@login_required
def lista_mensajes(request):
  lista = contacto_model.objects.all()
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  return render(request, 'panel_7c/lista.html',{'form':lista,'configuracion':ver_configuracion, 'mensajes':True})


@login_required
def ver_mensaje(request, p_id):
  ver_configuracion = get_object_or_404(panel_7c, pk=1)
  if request.method == 'GET':
    ver_mensaje = get_object_or_404(contacto_model, pk=p_id)
    return render(request, 'panel_7c/ver_mensaje.html',{'mensaje':ver_mensaje,'configuracion':ver_configuracion})
  else:
    return render(request, 'panel_7c/view_programa.html',{'configuracion':ver_configuracion, 'error':'algo fallo'})


@login_required
def eliminar_mensaje(request, p_id):
  lista = contacto_model.objects.all()
  if request.method == 'POST':
    try:
      ver = get_object_or_404(contacto_model, pk=p_id)
      ver.delete()
      return render(request, 'panel_7c/lista.html',{'form':lista, 'exito':'Se elimino correctamente', 'mensajes':True})
    except Exception as e:
      return render(request, 'panel_7c/lista.html',{'form':lista, 'error':e, 'mensajes':True})
  else:
      return render(request, 'panel_7c/lista.html',{'form':lista, 'error':'Algo paso'})











