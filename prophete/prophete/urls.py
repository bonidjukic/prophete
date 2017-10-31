# prophete URL Configuration

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from core.views import HomeView, PredictionView, calculate_forecast

urlpatterns = [
  url(
    r'^$',
    HomeView.as_view(),
    name='home'
  ),
  url(
    r'^data/(?P<prediction_pk>\d+)/$$',
    PredictionView.as_view(),
    name='prediction_view'
  ),
  url(
    r'^data/calculate/(?P<prediction_pk>\d+)/$$',
    calculate_forecast,
    name='calculate_forecast'
  ),
  url(
    r'^admin/',
    admin.site.urls
  ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)