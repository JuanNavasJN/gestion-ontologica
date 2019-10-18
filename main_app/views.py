from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Question, Result, UsuarioEvaluado
from gestion_project.utileria import render_pdf
from django.http import HttpResponse

class PDFAspirante(View):
    def get(self, request, *args, **kwargs):
        result_users = Result.objects.all()
        pdf = render_pdf("dashboard/userpdf.html", {'result_users':result_users})
        return HttpResponse(pdf, content_type="application/pdf")

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

def aspirantepdf(request):
    result_users = Result.objects.all()
    user_list = 37
    useraspirante = CustomUser.objects.get(id=user_list)
    pdf = render_pdf("dashboard/userpdf.html", {'result_users':result_users,'user_list' : user_list, 'useraspirante' : useraspirante})
    return HttpResponse(pdf, content_type="application/pdf")

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
    user_list = CustomUser.objects.all()
    result_users = Result.objects.all()
    usuariosev = UsuarioEvaluado.objects.all()
    if request.method == 'POST':
        if request.POST.get('generarpdf'):
            aspiranteid = request.POST.get('generarpdf')
            result_users = Result.objects.all()
            useraspirante = CustomUser.objects.get(id=aspiranteid)
            pdf = render_pdf("dashboard/userpdf.html", {'result_users':result_users, 'useraspirante' : useraspirante})
            return HttpResponse(pdf, content_type="application/pdf")
        else:
            return render(request, 'dashboard/evaluador/16pf.html', {'result_users' : result_users ,'user_list' : user_list} )
    return render(request, 'dashboard/evaluador/16pf.html', {'result_users' : result_users ,'user_list' : user_list, 'usuariosev': usuariosev} )

def ev_wartegg(request):
    return render(request, 'dashboard/evaluador/wartegg.html')

def ev_aspirante_16pf(request, id):
     return render(request, 'dashboard/evaluador/aspirante_16pf.html')

def ev_aspirante_wartegg(request, id):
     return render(request, 'dashboard/evaluador/aspirante_wartegg.html')

def aspirante_home(request):
    return render(request, 'dashboard/aspirante/home.html')

def aspirante_16pf(request):
    if request.method == 'POST':
        ls = Question.objects.all()
        if request.POST.get('puntos'):
            res=Result()
            res.points = request.POST.get('puntos')
            res.usuario = request.user.id
            #res.question= Question.objects.get(id=6)
            res.question = Question.objects.get(id=1)
            res.save()
        if request.POST.get('puntos2'):
            res=Result()
            res.points = request.POST.get('puntos2')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=2)
            res.save()
        if request.POST.get('puntos3'):
            res=Result()
            res.points = request.POST.get('puntos3')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=3)
            res.save()
        if request.POST.get('puntos4'):
            res=Result()
            res.points = request.POST.get('puntos4')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=4)
            res.save()
        if request.POST.get('puntos5'):
            res=Result()
            res.points = request.POST.get('puntos5')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=5)
            res.save()
        return redirect('aspirante_16pf2')
            #return HttpResponse('<h1>Registrada</h1>')
    else:
            ls = Question.objects.all()
            return render(request, 'dashboard/aspirante/test16pf.html', { 'ls': ls})

def aspirante_16pf2(request):
    if request.method == 'POST':
        ls = Question.objects.all()
        if request.POST.get('puntos6'):
            res=Result()
            res.points = request.POST.get('puntos6')
            res.usuario = request.user.id
            #res.question= Question.objects.get(id=6)
            res.question = Question.objects.get(id=6)
            res.save()
        if request.POST.get('puntos7'):
            res=Result()
            res.points = request.POST.get('puntos7')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=7)
            res.save()
        if request.POST.get('puntos8'):
            res=Result()
            res.points = request.POST.get('puntos8')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=8)
            res.save()
        if request.POST.get('puntos9'):
            res=Result()
            res.points = request.POST.get('puntos9')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=9)
            res.save()
        if request.POST.get('puntos10'):
            res=Result()
            res.points = request.POST.get('puntos10')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=10)
            res.save()
        return redirect('aspirante_16pf3')
    else:
            ls = Question.objects.all()
            return render(request, 'dashboard/aspirante/test16pf2.html', { 'ls': ls})

def aspirante_16pf3(request):
    if request.method == 'POST':
        ls = Question.objects.all()
        evaluado = UsuarioEvaluado()
        evaluado.identificador = request.user.id
        evaluado.nombre = request.user.first_name
        evaluado.apellido = request.user.last_name
        evaluado.cedula = request.user.username
        evaluado.save()
        if request.POST.get('puntos11'):
            res=Result()
            res.points = request.POST.get('puntos11')
            res.usuario = request.user.id
            #res.question= Question.objects.get(id=6)
            res.question = Question.objects.get(id=11)
            res.save()
        if request.POST.get('puntos12'):
            res=Result()
            res.points = request.POST.get('puntos12')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=19)
            res.save()
        if request.POST.get('puntos13'):
            res=Result()
            res.points = request.POST.get('puntos13')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=20)
            res.save()
        if request.POST.get('puntos14'):
            res=Result()
            res.points = request.POST.get('puntos14')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=21)
            res.save()
        if request.POST.get('puntos15'):
            res=Result()
            res.points = request.POST.get('puntos15')
            res.usuario = request.user.id
            res.question = Question.objects.get(id=22)
            res.save()
        return render(request, 'dashboard/aspirante/aspiranteend.html', { 'ls': ls})
    else:
            ls = Question.objects.all()
            return render(request, 'dashboard/aspirante/test16pf3.html', { 'ls': ls})

def aspiranteend(request):
    return render(request, 'dashboard/aspirante/aspiranteend.html')
    questions = range(1, 186)
    ls = Question.objects.all()
    return render(request, 'dashboard/aspirante/test16pf.html', { 'ls': ls}, { 'questions': questions})

#def del_16pf(request,id = None):
#    object = Question.objects.get(id=id)
#    object.delete()
#    ls = Question.objects.all()
#    return render(request,'dashboard/16pf.html', {'ls': ls})
