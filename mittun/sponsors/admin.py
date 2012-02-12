from django.contrib import admin

from sponsors.models import Sponsor, Category


class SponsorAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Category, CategoryAdmin)
