from django.db import models

class Folder(models.Model):
    name = models.TextField()
    date = models.DateField("date created")

class Entry(models.Model):
    date = models.DateTimeField("date created")
    content = models.TextField
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)