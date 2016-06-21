from __future__ import unicode_literals

from django.db import models


class PrimeModel(models.Model):
    n = models.IntegerField()
    ans = models.CharField(max_length=1000)


class GcdModel(models.Model):
    left = models.IntegerField()
    right = models.IntegerField()
    ans = models.CharField(max_length=1000)
