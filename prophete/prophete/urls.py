# prophete URL Configuration

from django.conf.urls import url
from django.contrib import admin
from core.views import HomeView

urlpatterns = [
  url(r'^$', HomeView.as_view(), name='home'),
  url(r'^admin/', admin.site.urls),
]
