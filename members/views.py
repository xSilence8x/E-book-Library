from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, LoginForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/registrace.html"
    success_url = reverse_lazy("prihlaseni")


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "registration/prihlaseni.html"
    success_url = reverse_lazy("home")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/upravit-profil.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user