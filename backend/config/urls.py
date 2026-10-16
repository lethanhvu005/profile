from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .views import frontend, uploaded_image, health
from portfolio.views import portfolio
urlpatterns=[path('admin/',admin.site.urls),path('api/portfolio/',portfolio)]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('',frontend),path('health/',health)]
if not settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<name>.+)$',uploaded_image)]
