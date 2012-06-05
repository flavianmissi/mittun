from django.contrib import admin

from mittun.sponsors.models import Sponsor, Category, Contact, Job, Requirement, Responsibility, Bonus


class ContactInline(admin.TabularInline):
    model = Contact


class ContactAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(ContactAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sponsor__user=request.user)

class JobAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(JobAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company__user=request.user)

class SponsorAdmin(admin.ModelAdmin):
    exclude = []

    inlines = [
        ContactInline,
    ]

    def queryset(self, request):
        qs = super(SponsorAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def change_view(self, request, object_id, *args, **kwargs):
        sponsor = Sponsor.objects.get(id=object_id)
        if request.user == sponsor.user:
            self.exclude.append('user')
        else:
            if 'user' in self.exclude:
                self.exclude.remove('user')
        return super(SponsorAdmin, self).change_view(request, object_id, *args, **kwargs)

    def add_view(self, *args, **kwargs):
        if 'user' in self.exclude:
            self.exclude.remove('user')
        return super(SponsorAdmin, self).add_view(*args, **kwargs)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Category)
admin.site.register(Job, JobAdmin)
admin.site.register(Responsibility)
admin.site.register(Requirement)
admin.site.register(Bonus)
