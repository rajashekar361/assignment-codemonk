from django.db import models


class Details(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    Pwd = models.CharField(max_length=200)
    dob = models.DateField()
    createdAt = models.DateField()
    modifiedAt = models.DateField(null=True)
