from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class LoginAnonymousView(UserPassesTestMixin, LoginView):
    def test_func(self):
        return self.request.user.is_anonymous


class LogoutPostView(LogoutView):
    http_method_names = ["post", "options"]
