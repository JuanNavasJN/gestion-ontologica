from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Question

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            if request.user.role == 2:
                return render(request, "dashboard/aspirante/home.html")
            else:
                return render(request, "dashboard/index.html")
        else:
            return redirect("/users/login/")

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
        #else:
        #    messages.error(request, 'Porfavor corriga el error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {
        'form': form
    })

def configuration(request):
    return render(request, 'dashboard/config.html')

def evaluators(request):
    evaluators = CustomUser.objects.filter(role=1)
    return render(request, 'dashboard/evaluadores.html', {'evaluators': evaluators})

def applicants(request):
    applicants = CustomUser.objects.filter(role=2)
    return render(request, 'dashboard/aspirantes.html', {'applicants': applicants})

def pfadmin(request):
    if request.method == 'POST':
        if request.POST.get('pregunta') and request.POST.get('factor'):
            post=Question()
            post.text = request.POST.get('pregunta')
            post.factor = request.POST.get('factor')
            post.points= 0
            post.complete= False
            post.save()
            ls = Question.objects.all()
            return render(request, 'dashboard/16pf.html', {'ls': ls} )
    else:
            ls = Question.objects.all()
            return render(request,'dashboard/16pf.html', {'ls': ls})

def ev_16pf(request):
    return render(request, 'dashboard/evaluador/16pf.html')

def ev_wartegg(request):
    return render(request, 'dashboard/evaluador/wartegg.html')

def ev_aspirante_16pf(request, id):
     return render(request, 'dashboard/evaluador/aspirante_16pf.html')

def ev_aspirante_wartegg(request, id):
     return render(request, 'dashboard/evaluador/aspirante_wartegg.html')

def aspirante_home(request):
    return render(request, 'dashboard/aspirante/home.html')

def aspirante_16pf(request):
    questions = range(1, 186)
    return render(request, 'dashboard/aspirante/test16pf.html', { 'questions': questions})
