
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('extendprofile.urls')),
    path('images/', include('images.urls', namespace='images')),
    # path('', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    # path('login', TemplateView.as_view(template_name='account/login.html'), name='login'),
    # path('accounts/', include('allauth.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)