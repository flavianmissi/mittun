from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView

from events.forms import BootstrapForm
from events.models import Event


class BaseCreateUpdateView(ModelFormMixin, ProcessFormView):

    def get(self, request, *args, **kwargs):
        self.set_object()
        return super(BaseCreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.set_object()
        return super(BaseCreateUpdateView, self).post(request, *args, **kwargs)

    def set_object(self):
        events = self.model.objects.all()

        if events.count():
            self.object = events[0]
        else:
            self.object = None


class BootstrapView(TemplateResponseMixin, BaseCreateUpdateView):

    model = Event
    form_class = BootstrapForm
    template_name = 'event_form.html'
    success_url = '/bootstrap'
