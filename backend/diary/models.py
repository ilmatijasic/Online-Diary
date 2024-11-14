from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField("date created")

    def __str__(self):
        return self.name

class Entry(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField("date created")
    content = models.TextField()

    def __str__(self):
        return self.name