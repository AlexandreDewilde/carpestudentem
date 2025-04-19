from django.shortcuts import render


# Create your views here.
def louvainpero_view(request):
    return render(request, "louvainpero/louvainpero.html")
