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
                  'genres',
                  'author',
                  'image',]
        widgets = {
            'name': forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'type': forms.Select(attrs = {'class':"form-select",'placeholder':""}),
            'volumenes': forms.TextInput(attrs = {'class':"form-control",'placeholder':""}),
            'published': forms.DateInput(attrs = {'type':"date",'class':"form-control",'placeholder':""}),
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
