from django.contrib import admin
from core.models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
  pass