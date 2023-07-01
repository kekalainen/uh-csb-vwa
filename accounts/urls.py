from django.urls import path

from .views import LoginAnonymousView

urlpatterns = [
    path("login/", LoginAnonymousView.as_view(), name="login"),
]
