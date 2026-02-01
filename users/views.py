from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroAlumnoForm
from django.contrib.auth.models import User
from .models import Perfil

@login_required
def dashboard(request):
    perfil=request.user.perfil
    return render(request, 'users/dashboard.html', {'perfil': perfil})

def registro_alumno(request):
    if request.method  == 'POST':
        form=RegistroAlumnoForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            user.save()

            perfil=user.perfil
            perfil.es_alumno=True
            perfil.save()

            return render(request, 'users/registro_pendiente.html')
    else:
        form=RegistroAlumnoForm()
    
    return render(request, 'users/registro.html', {'form': form})

def es_admin(user):
    return hasattr(user, 'perfil') and user.perfil.es_admin

@user_passes_test(es_admin)
def aprobar_alumnos(request):
    if request.method == 'POST':
        perfil_id = request.POST.get('perfil_id')
        accion= request.POST.get('accion')

        perfil = Perfil.objects.get(id=perfil_id)

        if accion == 'aprobar':
            perfil.estado='aprobado'
            perfil.user.is_active=True
            perfil.user.save()

        elif accion == 'rechazar':
            perfil.estado='rechazado'
            perfil.user.is_active=False
            perfil.user.save()
        perfil.save()

        return redirect('aprobar_alumnos')
    
    pendientes=Perfil.objects.filter(
        es_alumno=True,
        estado='pendiente'
    )

    return render(
        request, 'users/aprobar_alumnos.html', {'pendientes':pendientes}
    )
