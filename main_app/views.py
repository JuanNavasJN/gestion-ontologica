from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

class EvaluadoresView(TemplateView):
    template_name = 'dashboard/evaluadores.html'

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Su contraseña ha sido actualizada exitosamente!')
            update_session_auth_hash(request, user)  # Important!

            return redirect('change_password')
        else:
            messages.error(request, 'Porfavor corriga el error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {
        'form': form
    })

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
