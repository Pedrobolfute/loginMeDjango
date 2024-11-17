from django.db import models

# Create your models here.

class User(models.Model):
    name_user = models.CharField(max_length=50, blank=False, null=False)
    password_user = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.name_user


class Animal(models.Model):
    specie_animal = models.CharField(max_length=50, blank=True, null=True)
    color_animal = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animal')

    def __str__(self) -> str:
        return self.specie_animal


class Vehicle(models.Model):
    mark_vehicle = models.CharField(max_length=50, blank=True, null=True)
    model_vehicle = models.CharField(max_length=50, blank=True, null=True)
    year_vehicle = models.IntegerField(blank=True, null=True)
    color_vehicle = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle')

    def __str__(self) -> str:
        return self.model_vehicle


class Job(models.Model):
    company_job = models.CharField(max_length=50, blank=True, null=True)
    position_job = models.CharField(max_length=50, blank=True, null=True)
    salary_job = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job')

    def __str__(self) -> str:
        return self.position_job


class Document(models.Model):
    type_document = models.CharField(max_length=50, blank=True, null=True)
    number_document = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document')


    def __str__(self) -> str:
        return self.type_document