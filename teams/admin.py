from django.contrib import admin
from .models import Team, Member


class MemberInline(admin.TabularInline):
    model = Member
    extra = 1

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    inlines = [MemberInline]

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'team')
    list_filter = ('team', 'role')
    search_fields = ('first_name', 'last_name', 'nickname')
