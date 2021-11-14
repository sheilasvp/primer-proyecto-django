from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name=}, {self.balance=}"


class Transaction(models.Model):
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    amount = models.FloatField(default=0.0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
