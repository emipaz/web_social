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
        
    def clean_contraseña2(self):
        cd = self.cleaned_data
        if cd['contraseña'] != cd['contraseña2']:
            self.add_error('contraseña', 
                           forms.ValidationError('Las contraseñas no coinciden.'))
            #self.add_error('contraseña2', "Las contraseñas no coinciden")
            # raise forms.ValidationError("Las contrasenias no coinciden")
        return  cd["contraseña2"]
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            self.add_error("email", 
                forms.ValidationError(f'El mail {data} ya se encuentra registrado.'))
        return data
    
    
    
    
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email']
        
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id)\
                     .filter(email=data)
        if qs.exists():
            self.add_error("email", 
                forms.ValidationError(f'El mail {data} ya se encuentra registrado.'))
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['fecha_nacimiento', 'foto']
