from django.contrib.auth.mixins import UserPassesTestMixin


class UserIsAnonymousMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous


class UserOwnsObjectMixin(UserPassesTestMixin):
    object_owner_field_name = "owner"

    def test_func(self):
        obj = self.get_object()
        obj_owner = getattr(obj, self.object_owner_field_name)

        return self.request.user == obj_owner
