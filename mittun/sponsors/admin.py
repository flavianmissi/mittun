from django.contrib import admin

from mittun.sponsors.models import Sponsor, Category, Contact, Job


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

class JobAdmin(admin.ModelAdmin):
    pass


if Contact not in admin.site._registry:
    admin.site.register(Contact, ContactAdmin)
if Sponsor not in admin.site._registry:
    admin.site.register(Sponsor, SponsorAdmin)
if Category not in admin.site._registry:
    admin.site.register(Category, CategoryAdmin)
if Job not in admin.site._registry:
    admin.site.register(Job, JobAdmin)
