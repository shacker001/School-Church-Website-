from django.urls import path
from .views import contact_view
from . import views

urlpatterns = [
    path('', contact_view, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
