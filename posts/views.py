from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("content",)
    http_method_names = ["post", "options"]
    success_url = reverse_lazy("posts:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    ordering = "-updated_at"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        create_view = PostCreateView()
        context["form"] = create_view.get_form_class()

        return context
