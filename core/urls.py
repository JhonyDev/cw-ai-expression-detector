from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static
from core import settings


def redirect_view(request):
    return redirect('/accounts/login/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_view, name='home'),
    path('website/', include('src.website.urls', namespace='website')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('src.accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
