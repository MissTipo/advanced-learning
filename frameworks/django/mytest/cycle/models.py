from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Period(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    length = models.IntegerField()
    symptoms = models.CharField(max_length=1000)
    end_date = models.DateField()

    def __str__(self):
        return f'Period: start date: {self.start_date}, end date: {self.end_date}, symptoms: {self.symptoms}'
