from django.contrib import admin
from .models import Company, Deal, Contact, CompanyNote, DealNote, ContactNote

from django.conf import settings

User = settings.AUTH_USER_MODEL


class DealInline(admin.TabularInline):
    model = Deal
    extra = 0


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    inlines = [DealInline, ContactInline]


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyNote)
admin.site.register(ContactNote)
admin.site.register(DealNote)
admin.site.register(Contact)
admin.site.register(Deal)
