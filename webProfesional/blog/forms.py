from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre',min_length=3,required=True,widget=forms.TextInput(attrs={'placeholder': 'Escriba su nombre...','class': 'form-control my-2'}))
    email = forms.EmailField(max_length=200,label='Email',min_length=3,required=True,widget=forms.TextInput(attrs={'placeholder': 'Escriba su Email...','class': 'form-control my-2'}))
    to = forms.EmailField(max_length=200,label='Para:',min_length=3,required=True,widget=forms.TextInput(attrs={'placeholder': 'Escriba el Email a compartir..','class': 'form-control my-2'}))
    comments = forms.CharField(max_length=1000,label='Comentario',min_length=3,required=True,widget=forms.Textarea(attrs={'placeholder': 'Escriba uncomentario...','class': 'form-control mb-3 ml-3 my-2', 'rows':3}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Escriba su nombre...'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Escriba su email...' }),
             'body': forms.Textarea(
                attrs={'class': 'form-control mb-3 mr-3', 'required': 'True', 'placeholder': 'Escriba su comentario...', 'rows':'5' }),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Email',
            'body': 'Comentario',
        }

class ReplyCommentPostForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre',min_length=3,required=True,widget=forms.TextInput(attrs={'placeholder': 'Escriba su nombre...','class': 'form-control my-2'}))
    email = forms.EmailField(max_length=200,label='Email',min_length=3,required=True,widget=forms.TextInput(attrs={'placeholder': 'Escriba su Email...','class': 'form-control my-2'}))
    body = forms.CharField(max_length=1000,label='Body',min_length=3,required=True,widget=forms.Textarea(attrs={'placeholder': 'Escriba su respuesta...','class': 'form-control mb-3 ml-3 my-2', 'rows':3}))



class SearchForm(forms.Form):
    query = forms.CharField(max_length=100,label='',min_length=3,required=True,widget=forms.TextInput(attrs={'placeholder': 'Search..','class': 'form-control','type': 'text'}))

