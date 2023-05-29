from django import forms
from .models import ContactUs

class ContacUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["full_name", "email", "subject", "message"]
        
        
        
