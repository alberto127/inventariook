from django.conf.urls import url, include
from apps.usuarios.views import UsuariosList, usuario_nuevo, posts
from . import views

urlpatterns = [

   url(r'^listar$', UsuariosList.as_view(), name='usuario_listar'),
   #url(r'^nuevo$', views.usuario_nuevo, name='usuario_nuevo'),
   #url(r'^listar_prueba$', views.posts, name='listar'),
   #url(r'^nuevo/add$', views.add_usuario, name='add_usuario'),
   #url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
   #url(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]