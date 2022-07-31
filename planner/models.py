from django.db import models


class Parent_Info(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name + self.last_name +(str)(self.phone_number)


class Child_Info(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    id_parent = models.ForeignKey(Parent_Info, on_delete=models.CASCADE)
    birthdate = models.DateField()

    def __str__(self):
        return self.first_name + self.last_name + self.patronymic
