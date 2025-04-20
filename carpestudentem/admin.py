from django.contrib import admin
from .models import Content, ContentImage, ContentButton, ProjectsPresentation, NavbarButtons


class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "content")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
    list_per_page = 20
    list_editable = ("content",)


class ContentImageAdmin(admin.ModelAdmin):
    list_display = ("name", "content")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
    list_per_page = 20
    list_editable = ("content",)


class ContentButtonAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "link")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
    list_per_page = 20
    list_editable = ("text", "link")


class ProjectsPresentationAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 20
    list_editable = ("description",)


class NavbarButtonsAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "link")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
    list_per_page = 20
    list_editable = ("text", "link")


admin.site.register(Content, ContentAdmin)
admin.site.register(ContentImage, ContentImageAdmin)
admin.site.register(ContentButton, ContentButtonAdmin)
admin.site.register(ProjectsPresentation, ProjectsPresentationAdmin)
admin.site.register(NavbarButtons, NavbarButtonsAdmin)