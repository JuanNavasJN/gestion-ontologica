from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dash', views.DashboardView.as_view(), name='dashboard'),
    path('dash/evaluadores', views.evaluators, name='evaluadores'),
    path('dash/aspirantes', views.applicants, name='aspirantes'),
    path('dash/16pf', views.pfadmin, name='16pfadmin'),
    path('dash/evaluador/16pf', views.ev_16pf, name='16pfevaluador'),
    path('dash/evaluador/wartegg', views.ev_wartegg, name='waterggevaluador'),
    path('dash/evaluador/16pf/<int:id>', views.ev_aspirante_16pf, name='16pfevaluador_aspirante'),
    path('dash/evaluador/wartegg/<int:id>', views.ev_aspirante_wartegg, name='waterggevaluador_aspirante'),
]