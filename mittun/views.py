from django.views.generic import TemplateView

from mittun.events.models import Event


class IndexView(TemplateView):

    template_name = 'index.html'


class AboutView(TemplateView):

    template_name = 'about.html'

    def get_object(self):
        return Event.objects.get(pk=1)

    def get_context_data(self):
        return {
            'event': self.get_object()
        }

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context=self.get_context_data)
