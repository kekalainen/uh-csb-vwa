from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView

class LoginAnonymousView(UserPassesTestMixin, LoginView):
    def test_func(self):
        return self.request.user.is_anonymous
