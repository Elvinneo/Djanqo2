from django.db import models

class Userss(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    addresstolive=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    specialty=models.TextField(max_length=50)
    age=models.CharField(max_length=20)
    hobbies=models.TextField(max_length=50)
    university=models.TextField(max_length=50)
    def __str__(self):
        return self.name

