from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'
    http_method_names = ['get']


class ContactView(AboutView):
    pass






