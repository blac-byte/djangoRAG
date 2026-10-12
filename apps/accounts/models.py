from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related='document')
    document = models.FileField(upload_to='uploads/')