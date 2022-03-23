from django.forms import ModelForm
from django import forms
from .models import User

class studentforms(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }