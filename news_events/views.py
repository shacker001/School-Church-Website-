from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import News, Event  # Make sure to import both models

def news_list(request):
    news_list = News.objects.all().order_by('-publication_date')
    events_list = Event.objects.all().order_by('-event_date')

    # Create Paginator instances
    paginator_news = Paginator(news_list, 5)  # Show 5 news items per page
    paginator_events = Paginator(events_list, 5)

    # Get the current page number from the GET request (default to page 1 if not specified)
    page_news = request.GET.get('page')
    page_events = request.GET.get('page')

    # Get the Page objects for the current page
    news = paginator_news.get_page(page_news)
    events = paginator_events.get_page(page_events)

    # Pass the paginated news and events to the template
    return render(request, 'news_events/news_list.html', {'news': news, 'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'news_events/event_detail.html', {'event': event})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_events/news_detail.html', {'news': news})