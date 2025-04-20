from django.contrib import admin

from .models import Couverture, CouvertureType


@admin.register(Couverture)
class CouvertureAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(CouvertureType)
class CouvertureTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
