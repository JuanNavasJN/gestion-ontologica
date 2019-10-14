from django.db import models

# Create your models here.
class Preguntas16pf(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    Preguntas16pf = models.ForeignKey(Preguntas16pf, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    points = models.IntegerField()
    complete = models.BooleanField()

    def __str__(self):
        return self.text
