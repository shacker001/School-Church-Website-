from django.shortcuts import render
from .models import Activity

def activities(request):
    activities = Activity.objects.all()
    return render(request, 'student_life/activities.html', {'activities': activities})
