from django.views.generic import CreateView

from events.forms import BootstrapForm
from events.models import Event


class BootstrapView(CreateView):

    model = Event
    form_class = BootstrapForm
    template_name = 'event_form.html'

    def get(self, request, *args, **kwargs):
        events = self.model.objects.all()
        if events.count():
            self.object = events[0]
        else:
            self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(form=form))
