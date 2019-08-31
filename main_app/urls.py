from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dash', views.DashboardView.as_view(), name='dashboard'),
    path('dash/evaluadores', views.EvaluadoresView.as_view(), name='evaluadores'),
    path('dash/aspirantes', views.AspirantesView.as_view(), name='aspirantes'),
]