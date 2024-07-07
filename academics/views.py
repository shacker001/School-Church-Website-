from django.shortcuts import render
from .models import Program

def programs(request):
    programs = Program.objects.all()
    return render(request, 'academics/programs.html', {'programs': programs})
