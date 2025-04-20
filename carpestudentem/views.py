from django.shortcuts import render

from .models import Content, ContentImage, ProjectsPresentation


def index(request):
    contents = {content.name: content.content for content in Content.objects.all()}
    contents_images = {
        content_image.name: content_image.content
        for content_image in ContentImage.objects.all()
    }
    return render(
        request,
        "index.html",
        {"contents": contents, "contents_images": contents_images},
    )
