from django import forms
from django.contrib.auth.models import User
from .models import Report
from django.forms import ModelForm, Textarea, CharField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        title = forms.CharField(initial='Your name')
        fields = ('title', 'pub_date', 'content')
        
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        initial = {
            'content': u'Init'
        }
        help_texts = {
            'content': 'Some useful help text.',
        }
