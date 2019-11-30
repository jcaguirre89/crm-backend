from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import (
    Deal,
    Contact,
    DealNote,
    ContactNote,
    Checklist,
    IC_Member,
    Status,
    Country,
    Industry,
    Sector,
)

User = get_user_model()


class ChecklistInline(admin.TabularInline):
    model = Checklist


class DealNoteInline(admin.TabularInline):
    model = DealNote
    extra = 0


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class DealAdmin(admin.ModelAdmin):
    inlines = [ChecklistInline, ContactInline, DealNoteInline]


admin.site.register(Country)
admin.site.register(Industry)
admin.site.register(Sector)
admin.site.register(Status)
admin.site.register(IC_Member)
admin.site.register(ContactNote)
admin.site.register(DealNote)
admin.site.register(Contact)
admin.site.register(Deal, DealAdmin)
