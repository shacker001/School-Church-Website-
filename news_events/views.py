from django.shortcuts import render
from .models import News, Event

def news_list(request):
    news = News.objects.all().order_by('-publication_date')
    return render(request, 'news_events/news_list.html', {'news': news})

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'news_events/event_list.html', {'events': events})
