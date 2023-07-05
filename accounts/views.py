from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from throttle.decorators import throttle

from .mixins import UserIsAnonymousMixin


class RegisterView(UserIsAnonymousMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/register.html"


@method_decorator(throttle(zone="accounts:login"), name="post")
class LoginAnonymousView(UserIsAnonymousMixin, LoginView):
    pass


class LogoutPostView(LogoutView):
    http_method_names = ["post", "options"]
