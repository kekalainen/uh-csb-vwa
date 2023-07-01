from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .mixins import UserIsAnonymousMixin


class RegisterView(UserIsAnonymousMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/register.html"


class LoginAnonymousView(UserIsAnonymousMixin, LoginView):
    pass


class LogoutPostView(LogoutView):
    http_method_names = ["post", "options"]
