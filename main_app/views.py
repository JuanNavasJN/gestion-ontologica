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

def ev_16pf(request):
    return render(request, 'dashboard/evaluador/16pf.html')

def ev_wartegg(request):
    return render(request, 'dashboard/evaluador/wartegg.html')

def ev_aspirante_16pf(request, id):
     return render(request, 'dashboard/evaluador/aspirante_16pf.html')
    
def ev_aspirante_wartegg(request, id):
     return render(request, 'dashboard/evaluador/aspirante_wartegg.html')