from django.db import models

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    points = models.IntegerField()
    author = models.CharField(max_length=10)
    publicationDate = models.TimeField()
    def __str__(self):
        return f"{self.title} published by {self.author} on {self.publicationDate}"

class Job(models.Model):
    title =  models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    publicationDate = models.TimeField()
    def __str__(self):
        return f"{self.title} published by {self.link} on {self.publicationDate}"