# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here

class Ranking(models.Model):
    rank = models.CharField(max_length=200)

    def __str__(self):
        return self.rank


class Questions(models.Model):
    questions = models.CharField(max_length=400)

    def __str__(self):
        return self.questions

class Answers(models.Model):
    rank = models.ForeignKey(Ranking, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answers = models.TextField(blank=True)

    def __str__(self):
        return self.answers


