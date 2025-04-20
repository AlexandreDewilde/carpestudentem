from django.shortcuts import render

from carpestudentem.models import Content, ContentImage
from .models import Edition, Sponsor

# Create your views here.
def louvainpero_view(request):
    content = {content.name: content.content for content in Content.objects.all()}
    content_images = {content_image.name: content_image.content for content_image in ContentImage.objects.all()}
    last_edition = Edition.objects.order_by("-year").first()
    sponsors = Sponsor.objects.filter(edition=last_edition)
    previous_editions = Edition.objects.exclude(year=last_edition.year).order_by("-year")
    return render(request, "louvainpero/louvainpero.html", {"content": content, "last_edition": last_edition, "sponsors": sponsors, "previous_editions": previous_editions, "content_images": content_images})
