from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Period(models.Model):
    start_date = models.DateField()
    length = models.IntegerField()
    symptoms = models.CharField(max_length=1000)
    end_date = models.DateField()

    def __str__(self):
        return self.start_date
