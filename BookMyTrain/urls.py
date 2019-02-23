from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^first_app/', include('first_app.urls')),
    url(r'^CheckStatus/', include('CheckStatus.urls')),
    url(r'^FindTrains/', include('FindTrains.urls')),
    url(r'^tickets/', include('tickets.urls')),
    url(r'admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
