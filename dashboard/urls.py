from django.urls import path

from . import views

urlpatterns = [
    path('dash', views.HomePageView.as_view(), name='index'),
    path('', views.LoginPageView.as_view(), name='login')
    # path('dashboard', views.DashboardView.as_view(), name='dashboard'),
]
