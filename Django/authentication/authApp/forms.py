from django import forms

class loginForm(forms.Form):
    """A class for logging in form"""

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())