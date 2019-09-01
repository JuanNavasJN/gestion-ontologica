from django.urls import path

from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin/add_evaluator', views.add_evaluator, name='add_evaluator'),
    path('admin/add_applicant', views.add_applicant, name='add_applicant'),
    path('admin/update_user', views.update_user, name='update_user'),
    path('admin/delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('admin/evaluators', views.get_evaluators, name='get_evaluators'),
    path('admin/applicants', views.get_applicants, name='get_applicants'),
    path('admin/user/<int:id>', views.get_user, name='get_user'),
]
