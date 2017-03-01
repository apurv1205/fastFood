import re
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class ReviewForm(forms.Form):
    CHOICES = (('1', '1'), ('2', '2'),('3', '3'), ('4', '4'),('5', '5'))
    review = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=100,rows=3,
                                  cols=40)),label="Review")
    rating = forms.ChoiceField(choices=CHOICES, label=_("Rating"))

class StatusForm(forms.Form):
    CHOICES = (('1', 'Confirmed',), ('2', 'Preparing',),('3', 'Out for delivery',), ('4', 'Delivered',))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,label=_("Select status"))

class PostForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"))
    price = forms.IntegerField(required=True, min_value=1, label=_("Price"), error_messages={ 'invalid': ("Enter valid price") })
    cuisine = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Cuisine"))
    category = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Category"))

class RegistrationForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"))
    username = forms.RegexField(regex=r'^\d{10}$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Contact"), error_messages={ 'invalid': ("Enter a 10 digit number") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("This Contact already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
class RegistrationRestForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"))
    username = forms.RegexField(regex=r'^\d{10}$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Contact"), error_messages={ 'invalid': ("Enter a 10 digit number") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    address = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=100,rows=3,style='resize:none;')),label="Address")
    website = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Website"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("This Contact already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class AddressForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=100,rows=3,
                                  cols=40)),label="Delivery address")
