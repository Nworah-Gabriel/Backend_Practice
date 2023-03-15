from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
# Create your views here.
class loginView(View):
    """A class that handles the login view"""
    form_class = loginForm

    def get(self, req, *args, **kwargs):
        """A function for logging in"""
        form = self.form_class()
        return render(req, 'login.html', {'form':form})

    def post(self, req, *args, **kwargs):
        form = self.form_class(data=req.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return HttpResponse('You successfully logged in!')
            else:
                return HttpResponse('You credentials are not correct!')
        else:
            return HttpResponse('The form is not valid')


class logoutView(View):
    """A class that handles the logout view"""

    def get(self, req, *args, **kwargs):
        """A function for logging out"""
        user = req.user
        if isinstance(user, AnonymousUser):
            return HttpResponse('You\'re not logged in!!!')
        else:
            logout(req)
            return HttpResponse('You\'ve successfully logged out :)')
        return HttpResponse("Logout view")


class protectedView(View):
    """A class that handles the protected view"""

    def get(self, req, *args, **kwargs):
        """A function for getting protected information"""
        
        return HttpResponse("protected view")