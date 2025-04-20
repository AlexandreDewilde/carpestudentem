from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Material, LocationMaterial

def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            materials = form.cleaned_data.get('materials')
            form.save()
            for material in materials:
                location_material = LocationMaterial.objects.create(material=material, location=form.instance)
                location_material.save()
            return render(request, 'location/success.html', {'form': form})
    else:
        form = LocationForm()

    materials = Material.objects.all()
    return render(request, 'location/location.html', {'form': form, 'materials': materials})
