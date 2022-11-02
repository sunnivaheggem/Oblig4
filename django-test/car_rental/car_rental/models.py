from django.db import models

class Car(models.Model):
    make = models.CharField(max_length = 50) 
    carmodel = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.make + ' '+ + self.carmodel

class Customer(models.Model):
    name = models.CharField(max_length = 50) 
    age = models.CharField(max_length = 3)
    address = models.CharField(max_length = 50) 

    def __str1__(self):
        return self.name + ' '+ + self.age + ' '+ + self.address

class Employee(models.Model):
    name = models.CharField(max_length = 50) 
    branch = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50) 

    def __str2__(self):
        return self.name + ' '+ + self.branch + ' '+ + self.address