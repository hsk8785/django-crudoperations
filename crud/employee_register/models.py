from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    ID = models.CharField(max_length=100)
    fullname = models.CharField( max_length=100)
    mobile = models.CharField( max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)