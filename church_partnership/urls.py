from django.urls import path
from . import views

urlpatterns = [
    path('', views.church_partnership, name='church_partnership'),
]
