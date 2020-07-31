from django.db import models


class MonthlyStats(models.Model):
    revenue = models.IntegerField()
    cost = models.IntegerField()
    month = models.DateField()
