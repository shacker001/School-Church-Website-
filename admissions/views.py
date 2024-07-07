from django.shortcuts import render
from .models import AdmissionStep, ImportantDate

def admissions(request):
    steps = AdmissionStep.objects.all().order_by('step_number')
    dates = ImportantDate.objects.all().order_by('date')
    return render(request, 'admissions/admissions.html', {'steps': steps, 'dates': dates})
