from django.contrib.auth.models import User
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from cardinalwebdev_app.models import *

class ApplyForm(forms.Form):
    name       = forms.CharField(required=True, max_length=255)
    email      = forms.EmailField(required=True, max_length=254)
    major      = forms.CharField(required=True, max_length=255)
    attendance = forms.BooleanField(required=False)
    interest   = forms.CharField(required=True, widget=forms.Textarea)
    background = forms.CharField(required=True, widget=forms.Textarea)
    comments   = forms.CharField(required=False, widget=forms.Textarea)