from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm    , FormularioRegistroUsuario ,\
                   UserEditForm , ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

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
        
@login_required
def dashboard(request):
    return render(request,
                template_name = 'account/dashboard.html',
                context       = {'section': 'dashboard'})
    
def register(request):
    if request.method == 'POST':
        formulario_usuario = FormularioRegistroUsuario(request.POST)
        if formulario_usuario.is_valid():
            # Cree un nuevo objeto de usuario pero evite guardarlo todavía
            nuevo_usuario = formulario_usuario.save(commit=False)
            # setea al password
            nuevo_usuario.set_password( formulario_usuario.cleaned_data['contraseña'] )
            # Save the User object
            nuevo_usuario.save()
            # Create the user profile
            Profile.objects.create(usuario=nuevo_usuario)
            messages.success(request, 'Su cuenta ha sido Creada con exito')
            return render(request,
                      template_name = 'account/register_done.html',
                      context       =  {'nuevo_usuario': nuevo_usuario})
        else:
            messages.error(request , 'Error al crear su cuenta')
            return render(request,
                      template_name = 'account/register.html',
                      context       = {'formulario_usuario': formulario_usuario})
    else:
        formulario_usuario = FormularioRegistroUsuario()
        return render(request,
                      template_name = 'account/register.html',
                      context       = {'formulario_usuario': formulario_usuario})

 
@login_required
def edit(request):
    if request.method == 'POST':
        user_form    = UserEditForm(instance    = request.user, data = request.POST)
        profile_form = ProfileEditForm(instance = request.user.profile,
                                       data     = request.POST,
                                       files    = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Su cuenta ha sido actualizada')
        else:
            messages.error(request , 'Error al actualizar su cuenta')
    else:
        user_form    = UserEditForm(   instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
        

    return render(request,
                      template_name = 'account/edit.html',
                      context       = { 'user_form'    : user_form,
                                        'profile_form' : profile_form})