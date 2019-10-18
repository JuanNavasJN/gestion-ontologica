from django.contrib import admin
from .models import Question, Result, UsuarioEvaluado
# Register your models here.
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(UsuarioEvaluado)
