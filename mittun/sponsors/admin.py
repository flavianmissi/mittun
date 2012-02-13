from django.contrib import admin

from sponsors.models import Sponsor, Category, Contact


class ContactInline(admin.TabularInline):
    model = Contact


class ContactAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):

    inlines = [
        ContactInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Category, CategoryAdmin)
