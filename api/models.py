from django.db import models

# Create your models here.

class Students(models.Model):
    username = models.CharField(max_length=20)
    rollno = models.CharField(max_length=20)
    email = models.EmailField()
    occupation = models.CharField(max_length=20)
    profile = models.CharField(max_length=2000) 
    def __str__(self) -> str:
        return self.username + ' ' + self.rollno