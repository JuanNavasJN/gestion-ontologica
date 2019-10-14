from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.PositiveIntegerField(null=True, blank=True)
    updated_password = models.BooleanField(null=True, blank=True)
    date_born = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=12)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    def get_role(self):
        return '%s' % (self.role)
    def get_updated_password(self):
        return '%s' % (self.updated_password)