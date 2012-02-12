from django.contrib import admin

from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):

    pass


admin.site.register(Sponsor, SponsorAdmin)
