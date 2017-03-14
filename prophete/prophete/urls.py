# prophete URL Configuration

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from core.views import HomeView

urlpatterns = [
  url(r'^$', HomeView.as_view(), name='home'),
  url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)