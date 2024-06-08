from django.db import models

class Userss(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    email=models.CharField(max_length=30,null=True)
    addresstolive=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    specialty=models.TextField(max_length=50)
    age=models.TextField(max_length=20,null=True)
    hobbies=models.TextField(max_length=50)
    university=models.TextField(max_length=50)
    def __str__(self):
        return self.name

