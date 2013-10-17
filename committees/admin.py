from django.contrib import admin

from committees.models import Committee, Membership


class MembershipInline(admin.TabularInline):
    model = Membership


class CommitteeAdminOptions(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'chair', 'vice_chair']}),
    ]
    inlines = [MembershipInline]

admin.site.register(Committee, CommitteeAdminOptions)
