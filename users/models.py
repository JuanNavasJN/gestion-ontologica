from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.PositiveIntegerField(null=True, blank=True)
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    def get_role(self):
        return '%s' % (self.role)