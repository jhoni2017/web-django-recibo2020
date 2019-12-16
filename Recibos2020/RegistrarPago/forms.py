from django import forms
from datetime import datetime

class RegistrarPagoAguaForm(forms.Form):
    codigo=forms.CharField(label="Codigo", max_length=8, required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))

    fecha=forms.DateField(label="Fecha", required=True, widget=forms.DateInput(
        attrs={'class':'form-control'}
    ))

    monto=forms.FloatField(label="Monto", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control'}
    ))

