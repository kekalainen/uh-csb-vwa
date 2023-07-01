from django.urls import path

from .views import RegisterView, LoginAnonymousView, LogoutPostView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAnonymousView.as_view(), name="login"),
    path("logout/", LogoutPostView.as_view(), name="logout"),
]
