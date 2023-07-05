from django.contrib.admin import site
from django.views.generic.edit import DeleteView

from throttle.decorators import throttle

_admin_site_login_throttled = throttle(zone="accounts:login")(site.login)


def admin_site_login_throttled_post(request):
    if request.method == "POST":
        return _admin_site_login_throttled(request)

    return site.login(request)


class GenericDeleteView(DeleteView):
    template_name="confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['model_name'] = self.object._meta.verbose_name
        context['list_item_template_name'] = "%s/_%s_list_item.html" % (self.object._meta.app_label, self.object._meta.verbose_name)

        return context
