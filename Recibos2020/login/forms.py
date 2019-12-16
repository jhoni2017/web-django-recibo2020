from django import forms

class LoginForm(forms.Form):
    usuario=forms.CharField(label="Usuario",max_length=20, required=True, widget=forms.TextInput(
        attrs={'class':'form-control'} 
    ))
    contraseña=forms.CharField(label="Contraseña",max_length=20, widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))