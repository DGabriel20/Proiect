from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    is_logged = models.BooleanField(default=False)

    def __str__(self):
        return f'User (name = {self.name}, email = {self.email})'
