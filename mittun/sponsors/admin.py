from django.contrib import admin

from sponsors.models import Sponsor, Category, Contact


class ContactAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Category, CategoryAdmin)
