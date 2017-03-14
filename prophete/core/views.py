from django.views.generic.base import TemplateView

class HomeView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    return context

  def post(self, request, *args, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    return super(HomeView, self).render_to_response(context)