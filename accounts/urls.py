from django.urls import path

from .views import LoginAnonymousView, LogoutPostView

urlpatterns = [
    path("login/", LoginAnonymousView.as_view(), name="login"),
    path("logout/", LogoutPostView.as_view(), name="logout"),
]
