from django import forms
from core.models import Prediction

class PredictionForm(forms.ModelForm):
  class Meta:
    model = Prediction
    fields = [ 'data_upload', 'col_ts', 'col_val', ]