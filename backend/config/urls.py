from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from portfolio.views import portfolio
urlpatterns=[path('admin/',admin.site.urls),path('api/portfolio/',portfolio)]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
