from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class LoginForm(forms.Form):
    usuario  = forms.CharField()
    password = forms.CharField( widget = forms.PasswordInput)
    

class FormularioRegistroUsuario(forms.ModelForm):
    contraseña  = forms.CharField( widget = forms.PasswordInput , label = "Contraseña")
    contraseña2 = forms.CharField( widget = forms.PasswordInput,  label = "Repita Contraseña")
    
    class Meta():
        model = User
        fields = ['username','email','first_name','last_name']
        
    def limpiar_contraseña(self):
        
        cd = self.clean_data
        if cd['contraseña'] != cd['contraseña2']:
            raise forms.ValidationError("Las contrasenias no coinciden")
        return cd["contraseña"]
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['fecha_nacimiento', 'foto']
