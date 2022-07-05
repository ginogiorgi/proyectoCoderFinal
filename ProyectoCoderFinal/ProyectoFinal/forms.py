from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class MangaForm(forms.ModelForm):
    
    class Meta:
        model = Manga
        fields = ['name',
                  'type',
                  'volumenes',
                  'published',
                  'status',
                  'description',
                  'background',
                  'genres',
                  'author',
                  'image',]
        widgets = {
            'name': forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'type': forms.Select(attrs = {'class':"form-select",'placeholder':""}),
            'volumenes': forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'published': forms.DateInput(attrs = {'type':"date",'class':"form-control",'placeholder':""}),
            'description': forms.Textarea(attrs = {'class':"form-control",'placeholder':""}),
            'background': forms.Textarea(attrs = {'class':"form-control",'placeholder':""}),
            'status': forms.Select(attrs = {'class':"form-select",'placeholder':""}),
            'genres': forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'author': forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'image': forms.FileInput(attrs = {'class':"form-control",'placeholder':""}),
        }


class AnimeForm(forms.ModelForm):
       
    class Meta:
        model = Anime
        fields = ['name', 
                  'type', 
                  'episodes', 
                  'relase_date', 
                  'studio', 
                  'genres', 
                  'duration', 
                  'description', 
                  'backgroun', 
                  'image',]

        widgets = {
            'name':forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'type':forms.Select(attrs = {'class':"form-select", 'placeholder':""}),
            'episodes':forms.TextInput(attrs = {'class':"form-control", 'placeholder':""}),
            'relase_date':forms.DateInput(attrs = {'type':"date", 'class':"form-control", 'placeholder':""}),
            'studio':forms.Select(attrs = {'class':"form-select", 'placeholder':""}),
            'genres':forms.TextInput(attrs = {'class':"form-control", 'placeholder':""}),
            'duration':forms.TextInput(attrs = {'class':"form-control", 'placeholder':""}),
            'description':forms.Textarea(attrs = {'class':"form-control", 'placeholder':""}),
            'backgroun':forms.Textarea(attrs = {'class':"form-control", 'placeholder':""}),
            'image':forms.FileInput(attrs = {'class':"form-control", 'placeholder':""}),
        }


class StudiosForm(forms.ModelForm):

    class Meta:
        model = Studios
        fields = ['name',
                  'fundation_date',
                  'description',
                  'image',
                  ]
        widgets = {
            'name':forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'fundation_date' :forms.DateInput(attrs = {'type':"date", 'class':"form-control", 'placeholder':""}),
            'description':forms.Textarea(attrs = {'class':"form-control", 'placeholder':""}),
            'image':forms.FileInput(attrs = {'class':"form-control", 'placeholder':""}),
        }
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True, widget = forms.TextInput(attrs = {'class':"form-control",'placeholder':"Email"}))
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(attrs = {'class':"form-control",'placeholder':"Contraseña"}))
    password2 = forms.CharField(label= 'Confirmar contraseña', widget = forms.PasswordInput(attrs = {'class':"form-control",'placeholder':"Confirmar Contraseña"}))
    
    class Meta:
        model = User
        fields =  fields = ['first_name',
                            'last_name',
                            'username',
                            'email',
                            'password1',
                            'password2',
                            ]
        
        widgets = {'first_name': forms.TextInput(attrs = {'class':"form-control",'placeholder':"Nombre"}),
                   'last_name': forms.TextInput(attrs = {'class':"form-control",'placeholder':"Apellido"}),
                   'username': forms.TextInput(attrs = {'class':"form-control",'placeholder':"Nombre de Usuario"}),
        }
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class':"form-control",'placeholder':"Nombre de Usuario"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs ={'class':"form-control",'placeholder':"Contraseña"}))