from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('academics/', include('academics.urls')),
    path('admissions/', include('admissions.urls')),
    path('church_partnership/', include('church_partnership.urls')),
    path('news_events/', include('news_events.urls')),
    path('student_life/', include('student_life.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    