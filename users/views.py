from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    perfil=request.user.perfil
    return render(request, 'users/dashboard.html', {'perfil': perfil})
