from django.shortcuts import render
from couverture.forms import CouvertureForm

def couverture_view(request):
    if request.method == "POST":
        form = CouvertureForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, add a success message or redirect
    else:
        form = CouvertureForm()
    return render(request, 'couverture/couverture.html', {'form': form})
