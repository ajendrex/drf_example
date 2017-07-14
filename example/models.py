from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return "{}: {}".format(self.number, self.name)