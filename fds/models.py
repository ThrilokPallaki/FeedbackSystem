# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here

class Questions(models.Model):
    questions = models.CharField(max_length=400)


    def __str__(self):
        return self.questions

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    mobile_no = models.CharField(max_length=100)
    rank = models.CharField(max_length=200)

    def __str__(self):
        return self.rank


class Answers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
    rank = models.CharField(max_length=200)


    def __str__(self):
        return self.answers
