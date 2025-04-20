from django.contrib import admin

from .models import Edition, Sponsor


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ("name", "event_date")
    search_fields = ("name",)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name", "edition")
    search_fields = ("name",)
    list_filter = ("edition",)
    ordering = ("name",)
