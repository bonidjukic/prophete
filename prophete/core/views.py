from django.views.generic.base import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from core.forms import PredictionForm
from core.models import Prediction
from core.prophete import Prophete

class HomeView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    context['form'] = PredictionForm()
    return context

  def post(self, request, *args, **kwargs):
    form = PredictionForm(request.POST, request.FILES)
    form.full_clean()

    if form.is_valid():
      prediction = form.save()
      return redirect(reverse('prediction_view', kwargs={'prediction_pk': prediction.pk}))

    context = super(HomeView, self).get_context_data(**kwargs)
    context['form'] = form
    return super(HomeView, self).render_to_response(context)

class PredictionView(TemplateView):
  template_name = 'prediction_view.html'

  def get_context_data(self, **kwargs):
    prediction_pk = int(kwargs.get('prediction_pk', 0))
    prediction = get_object_or_404(Prediction, pk=prediction_pk)

    prophete = Prophete(prediction)
    prophete.predict(apply_log=True, periods=365)

    context = super(PredictionView, self).get_context_data(**kwargs)
    context['prediction'] = prediction
    return context

  def post(self, request, *args, **kwargs):
    pass