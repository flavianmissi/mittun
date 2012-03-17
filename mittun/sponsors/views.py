from django.views.generic import ListView

from mittun.sponsors.models import Sponsor


class SponsorsView(ListView):

    model = Sponsor
    template_name = 'sponsors_list.html'
