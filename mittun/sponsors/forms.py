from django.forms import ModelForm, ModelMultipleChoiceField

from mittun.sponsors.models import Job, Responsibility


class JobForm(ModelForm):

    responsabilities = ModelMultipleChoiceField(queryset=Responsibility.objects.all())

    class Meta:
        model = Job
