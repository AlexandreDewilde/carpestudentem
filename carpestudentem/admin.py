from django.contrib import admin
from .models import Content, ContentImage, ProjectsPresentation


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


class ProjectsPresentationAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 20
    list_editable = ("description",)


admin.site.register(Content, ContentAdmin)
admin.site.register(ContentImage, ContentImageAdmin)
admin.site.register(ProjectsPresentation, ProjectsPresentationAdmin)
