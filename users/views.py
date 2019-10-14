from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def add_user(data, option):
    if len(CustomUser.objects.filter(username=data['id'])) <= 0 :
        user = 2
        if option == "evaluator" :
            user = 1 

        u = CustomUser(username=data['id'], first_name=data['first_name'], last_name=data['last_name'], email=data['email'], role=user, date_born=data['date_born'], gender=data['gender'])
        u.set_password(data['id'])
        u.save()
        users = CustomUser.objects.all().values('id', 'username', 'first_name', 'last_name', 'email', 'role')
        users_list = list(users)
        return users_list
    else:
        return list()

@csrf_exempt
def add_evaluator(request):
    data = request.POST
    users_list = add_user(data, "evaluator")
    if len(users_list) > 0 :
        return JsonResponse(users_list, safe=False)
    else:
        return JsonResponse({"message": "User exists"})

@csrf_exempt
def add_applicant(request):
    data = request.POST
    users_list = add_user(data, "applicant")
    if len(users_list) > 0 :
        return JsonResponse(users_list, safe=False)
    else:
        return JsonResponse({"message": "User exists"})

@csrf_exempt
def update_user(request):
    data = request.POST
    print(data['gender'])
    user = CustomUser.objects.filter(id=data['id']).update(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], username=data['username'], gender=data['gender'], date_born=data['date_born'])
    users = CustomUser.objects.all().values('id', 'username', 'first_name', 'last_name', 'email', 'role')
    users_list = list(users)
    return JsonResponse(users_list, safe=False)

def delete_user(request, id=1):
    user = CustomUser.objects.filter(id=id).delete()
    users = CustomUser.objects.all().values('id', 'username', 'first_name', 'last_name', 'email', 'role')
    users_list = list(users)
    return JsonResponse(users_list, safe=False)

def get_evaluators(request):
    users = CustomUser.objects.filter(role=1).values('id', 'username', 'first_name', 'last_name', 'email', 'role')
    users_list = list(users)
    return JsonResponse(users_list, safe=False)

def get_applicants(request):
    users = CustomUser.objects.filter(role=2).values('id', 'username', 'first_name', 'last_name', 'email', 'role', 'date_born', 'gender')
    users_list = list(users)
    return JsonResponse(users_list, safe=False)

def get_user(request, id=1):
    user = CustomUser.objects.filter(id=id).values('id', 'username', 'first_name', 'last_name', 'email', 'role', 'date_born', 'gender')
    user = list(user)[0]
    return JsonResponse(user, safe=False)
