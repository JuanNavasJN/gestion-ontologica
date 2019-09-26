from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import CustomUser

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

class EvaluadoresView(TemplateView):
    template_name = 'dashboard/evaluadores.html'

def evaluators(request):
    evaluators = CustomUser.objects.filter(role=1)
    return render(request, 'dashboard/evaluadores.html', {'evaluators': evaluators})

def applicants(request):
    applicants = CustomUser.objects.filter(role=2)
    return render(request, 'dashboard/aspirantes.html', {'applicants': applicants})

def pfadmin(request):
    # applicants = CustomUser.objects.filter(role=2)
    return render(request, 'dashboard/16pf.html')