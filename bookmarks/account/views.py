from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            cd = formulario.cleaned_data
            user = authenticate(request,
                                username=cd['usuario'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticado exitosamente')
                else:
                    return HttpResponse('Cuenta deshabilitada')
            else:   
                return HttpResponse('Login Invalido')
    else:
        formulario = LoginForm()
        return render(request, 
                          template_name = 'account/login.html', 
                          context = {'form': formulario})