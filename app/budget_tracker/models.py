from django.db import models
from datetime import datetime


class House(models.Model):
    Id = models.IntegerField(primary_key=True)
    OwnerId = models.IntegerField()
    Name = models.CharField(max_length=50)
    Created = models.DateTimeField(default=datetime.now())
    Updated = models.DateTimeField(null=True)


class Budget(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Target = models.FloatField()
    Actual = models.FloatField()
    Created = models.DateTimeField(default=datetime.now())
    Updated = models.DateTimeField(null=True)
    House = models.ForeignKey(House, on_delete=models.CASCADE)


class BudgetItem(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=500, null=True)
    Target = models.FloatField()
    Actual = models.FloatField()
    Created = models.DateTimeField(default=datetime.now())
    Updated = models.DateTimeField(null=True)
    Budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
