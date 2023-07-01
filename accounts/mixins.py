from django.contrib.auth.mixins import UserPassesTestMixin


class UserIsAnonymousMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous
