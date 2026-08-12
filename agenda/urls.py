from django.urls import path, include  # add this
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('mopajendaadmin/', admin.site.urls),
    # Auth routes - login / register
    # path("", include("agendaapps.authentication.urls")),
    path("reg-agenda/", include("agendaapps.home.urls")),           # UI Kits Html files
    path("reg-agenda/", include("agendaapps.institute.urls")),
    path("reg-agenda/", include("agendaapps.event.urls")),
    path("reg-agenda/", include("agendaapps.custom.urls")),
    path("reg-agenda/", include("agendaapps.reports.urls")),
    path('summernote/', include('django_summernote.urls')),  # This is crucial
    
    path('api/', include('agendaapps.home.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    

   
