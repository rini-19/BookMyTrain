from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userDashboard/', views.user, name='userDashboard'),
    url(r'^first_app/', include('first_app.urls')),
    url(r'^registerpage/', views.Register_view, name='Register'),
    url(r'admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
