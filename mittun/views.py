from django.views.generic import ListView, TemplateView

from events.models import Event


class IndexView(ListView):

    model = Event
    template_name = 'index.html'
    context_object_name = 'event'


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
