from django.views.generic import TemplateView

class LoginPageView(TemplateView):
    template_name = 'dashboard/login.html'

class HomePageView(TemplateView):
    template_name = 'dashboard/index.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
