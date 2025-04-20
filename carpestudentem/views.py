from django.shortcuts import render
from django.forms.models import model_to_dict

from .models import Content, ContentImage, ContentButton, ProjectsPresentation


def index(request):
    contents = {content.name: content.content for content in Content.objects.all()}
    contents_images = {
        content_image.name: content_image.content
        for content_image in ContentImage.objects.all()
    }
    contents_buttons = {
        content.name: model_to_dict(content)
        for content in ContentButton.objects.all()
    }

    projects_presentation = ProjectsPresentation.objects.all()
    return render(
        request,
        "index.html",
        {"contents": contents, "contents_images": contents_images, "contents_buttons": contents_buttons, "projects_presentation": projects_presentation},
    )
