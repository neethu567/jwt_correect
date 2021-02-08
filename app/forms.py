from django import forms
from app.models import *
class CustomerForm(forms.ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Customer
        fields=['username','password']
        widgets = {
            'password': forms.PasswordInput()
        }