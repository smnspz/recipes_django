from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    profile_picture = models.URLField()
