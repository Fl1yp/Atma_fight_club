from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'number': forms.TextInput(attrs={'placeholder': '+79999999999'}),
        }
        labels = {
            'name': '',
            'number': '',
        }
