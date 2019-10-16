from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=300)
    factor = models.CharField(max_length=300)
    points = models.IntegerField()
    complete = models.BooleanField()

    def __str__(self):
        return self.text
