from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, null=True)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_no = models.CharField(max_length=8)
    flat_no = models.CharField(max_length=8, null=True)
    person = models.ForeignKey(Person)


class Phone(models.Model):
    phone_no = models.IntegerField
    type = models.CharField(max_length=64)
    person = models.ForeignKey(Person)
    

class Email(models.Model):
    email = models.CharField(max_length=64)
    person = models.ForeignKey(Person)


class Group(models.Model):
    name = models.CharField(max_length=64)
    people = models.ManyToManyField(Person)