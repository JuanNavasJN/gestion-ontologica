from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dash', views.DashboardView.as_view(), name='dashboard'),
    path('dash/evaluadores', views.evaluators, name='evaluadores'),
    path('dash/aspirantes', views.applicants, name='aspirantes'),
]