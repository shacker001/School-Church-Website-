from django.shortcuts import render
from .models import ChurchProgram, Testimonial

def church_partnership(request):
    programs = ChurchProgram.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'church_partnership/church_partnership.html', {'programs': programs, 'testimonials': testimonials})
