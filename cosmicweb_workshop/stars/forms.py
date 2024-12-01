from django import forms
from .models import Star

class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = ['name', 'constellation', 'magnitude', 'description', 'discovered_by']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }