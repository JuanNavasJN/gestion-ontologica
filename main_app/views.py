from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

class EvaluadoresView(TemplateView):
    template_name = 'dashboard/evaluadores.html'

class AspirantesView(TemplateView):
    template_name = 'dashboard/aspirantes.html'
