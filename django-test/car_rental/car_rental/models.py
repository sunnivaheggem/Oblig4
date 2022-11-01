from django.db import models

class Car(models.Model):
    make = models.CharField(max_length = 50) 
    carmodel = models.CharField(max_length = 50)

    def __str__(self):
        return self.make + ' '+ + self.carmodel

class Customer(models.Model):
    name = models.CharField(max_length = 50)
    age = models.CharField(max_length = 2)
    address = models.CharField(max_length = 50)


class Employee(models.Model):
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50) 
