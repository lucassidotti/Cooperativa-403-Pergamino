from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dashboard, registro_alumno, aprobar_alumnos

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('registro/', registro_alumno, name='registro'),
    path('aprobar/', aprobar_alumnos, name='aprobar_alumnos'),
]