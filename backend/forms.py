# forms.py
from django import forms
from .models import *
from django.forms import TextInput, Textarea, FileInput

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['title', 'description', 'image', ]  # Include all fields you want to edit
        widgets = { 

            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 500px; border: none; padding-bottom: 19px; background: transparent;',
                'placeholder': 'Hero Title'
                }),

            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 575px; margin-bottom:0px; background: transparent;',
                'placeholder': 'Description',
                'rows': 6,
                
                }),

            

        }

class CtaForm(forms.ModelForm):
    class Meta:
        model = Cta
        fields = ['title', 'description', ]  # Include all fields you want to edit
        widgets = { 

            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'width: max-width; border: none; padding-bottom: 19px; background: transparent;',
                'placeholder': 'Call To Action Title'
                }),

            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'width: max-width; margin-bottom:0px; background: transparent;',
                'placeholder': 'Description',
                'rows': 6,
                
                }),

            

        }

class AboutusForm(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = ['title', 'description', 'image', ]  # Include all fields you want to edit
        widgets = { 

            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 500px; border: none; padding-bottom: 19px; background: transparent;',
                'placeholder': 'About Us Title'
                }),

            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 575px; margin-bottom:0px; background: transparent;',
                'placeholder': 'Description',
                'rows': 6,
                
                }),

            

        }

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question', 'answer', ]  # Include all fields you want to edit
        widgets = { 

            'question': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; border: none; padding-bottom: 19px; background: transparent;',
                'placeholder': 'Question'
                }),

            'answer': Textarea(attrs={
                'class': "form-control",
                'style': 'width: max-width; margin-bottom:0px; background: transparent;',
                'placeholder': 'Answer',
                'rows': 6,
                
                }),

            

        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['description', 'image', ]  # Include all fields you want to edit
        widgets = { 

            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 495px; margin-bottom:0px; background: transparent;',
                'placeholder': 'Description',
                'rows': 6,
                
                }),

            

        }