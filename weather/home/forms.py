# forms.py

from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class WeatherInfoForm(forms.Form):
    city = forms.CharField(label='City Name', max_length=100)
