from django.contrib import admin

from mittun.events.models import Location, Event


class EventAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
