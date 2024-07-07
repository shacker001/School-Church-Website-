from django.shortcuts import render
from .models import History, MissionStatement

def about(request):
    history = History.objects.first()
    mission = MissionStatement.objects.first()
    return render(request, 'about/about.html', {'history': history, 'mission': mission})
