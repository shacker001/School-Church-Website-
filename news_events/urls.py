from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),  # List news and events
    path('news/<int:pk>/', views.news_detail, name='news_detail'),  # Detail view for news
    path('events/<int:pk>/', views.event_detail, name='event_detail'),  # Detail view for events
]
