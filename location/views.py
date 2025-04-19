from django.shortcuts import render, redirect
from .forms import LocationForm

def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location')  # Replace 'location' with the name of your success URL or view
    else:
        form = LocationForm()
    return render(request, 'location/location.html', {'form': form})
