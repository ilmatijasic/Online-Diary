from django.db import models
from django.conf import settings

class Folder(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    date = models.DateField("date created")

    def __str__(self):
        return self.name

class Entry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField("date created")
    content = models.TextField()

    def __str__(self):
        return self.name