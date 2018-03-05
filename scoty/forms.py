from django import forms
from .models import NewForm

class NewNewFormForm(forms.ModelForm):
    class Meta:
        model = NewForm
        exclude = []
        widgets = {
            
        }
