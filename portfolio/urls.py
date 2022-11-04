from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('register/', views.registro, name='registro'),
  path('login/', views.logear, name='logear'),
  path('logout/', views.deslogear, name='deslogear'),
  path('new/', views.add_programa, name='add_programa'),
  path('list/', views.lista_programas, name='lista'),
  path('read/<int:p_id>/', views.ver_programa, name='ver_programa'),
  path('read/<int:p_id>/delete/', views.eliminar_programa, name='eliminar_programa'),
  path('project/<int:p_id>/', views.ver_project, name='project'),
  path('contacto/', views.contacto, name='contacto'),
  path('panel_7c/', views.panel_7c_v, name='panel_7c'),
  path('mensajes/', views.lista_mensajes, name='mensajes'),
  path('mensaje/<int:p_id>/', views.ver_mensaje, name='ver_mensaje'),
  path('mensaje/<int:p_id>/delete/', views.eliminar_mensaje, name='eliminar_mensaje'),
]
