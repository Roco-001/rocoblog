from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control my-2', 'placeholder': 'Escribe tu nombre',
                       'required': 'required', 'type': 'text'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control my-2', 'placeholder': 'Escribe tu Email',
                       'required': 'required', 'type': 'text'}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control my-2', 'placeholder': 'Escribe el Asunto',
                       'required': 'required', 'type': 'text'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control my-4', 'placeholder': 'Mensaje',
                       'required': 'required', 'type': 'textarea', 'rows':'5'}),
        }
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'fecha': '',
            'content': '',
        }