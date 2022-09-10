from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    password1 = models.CharField(max_length=30, null=False, blank=False)
    password2 = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.username
