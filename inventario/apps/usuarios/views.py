from django.shortcuts import render

#from tables import PostTable

from django.http import HttpResponse, HttpResponseRedirect
from apps.usuarios.models import Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse_lazy
from apps.usuarios.forms import UsuarioForm
import json

# Create your views here.

class UsuariosList(ListView):
	model=Usuario
	template_name='personas/personas_list.html'

	def get_queryset(self):
		return Usuario.objects.all().order_by('usuario')

def posts(request):
	posts = PostTable()
	return render(request, "personas/listar.html", {'posts': posts})


def usuario_nuevo(request):
	#if request.method=='POST':
		nombre = request.POST.get('nombre', None)
		departamento = request.POST.get('departamento', None)
		email = request.POST.get('email', None)
		fc = request.POST.get('fuera_convenio', None)

		try:
			user_nuevo= Usuario(usuario = nombre, departamento = departamento, email = email, fuera_convenio = fc)
			user_nuevo.save()
			#return HttpResponseRedirect(reverse_lazy('usuarios:usuario_listar'))
			#return render(request, 'personas/personas_list.html')
			#return HttpResponse(json.dumps({"mensaje": "Usuario guardado exitosamente."}), content_type='application/json')
			return HttpResponse(json.dumps({"mensaje": "Usuario guardado exitosamente."}), content_type='application/json')
		except:
			#return HttpResponseRedirect(reverse_lazy('usuarios:usuario_listar'))
			return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')
	#else:
	#	form=UsuarioForm()
	#	return render(request, 'personas/personas_add.html')

#def usuario_nuevo(request):
#	model=Usuario
#	template_name='personas/personas_form.html'
#	form=UsuarioForm
#	success_url=reverse_lazy('usuarios:usuario_listar')


#def add_usuario(request):
#	if request.method=='POST':
#		form=UsuarioForm(request.POST)
#		if form.is_valid():
#			user=form.save(commit=False)
#
#			user.save()
#			return HttpResponseRedirect(reverse_lazy('usuarios:usuario_listar'))
#		else:
#			return render(request, 'personas/personas_add.html', {'form' : form})
#	else:
#		form=UsuarioForm()
#		context={}
#		return render(request, 'personas/personas_add.html', context)

#class UsuariosCreate(CreateView):
#	model=Usuario
#	form_class=UsuarioForm
#	template_name='personas/personas_form.html'
#	success_url=reverse_lazy('usuarios:usuario_listar')

    #def get_form_kwargs(self):
    #   kwargs = super().get_form_kwargs()
    #   kwargs.update({'request': self.request})
    #   return kwargs