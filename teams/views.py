from django.shortcuts import render
from .models import Team

def latest_team_view(request):
    latest_team = Team.objects.order_by('-year').first()
    return render(request, 'teams/teams.html', {'latest_team': latest_team})

