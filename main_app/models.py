from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=300)
    factor = models.CharField(max_length=300)
    points = models.IntegerField()
    complete = models.BooleanField()

    def __str__(self):
        return self.text

    def cualesId(self):
        return self.id

class Result(models.Model):
    usuario = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return str(self.question)

class UsuarioEvaluado(models.Model):
    identificador=models.IntegerField()
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    cedula = models.IntegerField()

    def __str__(self):
        return self.nombre
