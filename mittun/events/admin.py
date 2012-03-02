from django.contrib import admin

from mittun.events.models import Location


class LocationAdmin(admin.ModelAdmin):
    pass


if Location not in admin.site._registry:
    admin.site.register(Location, LocationAdmin)
