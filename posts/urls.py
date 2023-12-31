from django.urls import path

from .views import PostCreateView, PostDeleteView, PostListView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
]
