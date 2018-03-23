# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here


RANK_CHOICES = (('Excellent', 'Excellent'),('Good', 'Good'),('Average', 'Average'),('Worst', 'Worst'),)

class Questions(models.Model):
    questions = models.CharField(max_length=400)


    def __str__(self):
        return self.questions

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    mobile_no = models.CharField(max_length=100)
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)

    def get_absolute_url(self):
        return reverse('fds:thankyou', kwargs={'user':self.pk})

    def __str__(self):
        return self.user_name

class Answers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.TextField(blank=True)
    rank = models.CharField(max_length=200, choices=RANK_CHOICES)

    def __str__(self):
        return self.answer
