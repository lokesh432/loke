from django.db import models

# Create your models here.
class Student(models.Model):
    sn=models.IntegerField()
    sname=models.CharField(max_length=26)
    smarks=models.IntegerField()

    def  __str__(self):
        return self.sname