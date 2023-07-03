from django.views.generic.edit import DeleteView


class GenericDeleteView(DeleteView):
    template_name="confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['model_name'] = self.object._meta.verbose_name
        context['list_item_template_name'] = "%s/_%s_list_item.html" % (self.object._meta.app_label, self.object._meta.verbose_name)

        return context
