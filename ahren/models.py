# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Sheet(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    url = models.FileField()
    deleted = models.IntegerField(default = 1)
    
    @staticmethod
    def search(param):
        all = Sheet.objects.all()
        for x in range (len(all)):
            new = all[x]
            if new.name == param:
                return new
