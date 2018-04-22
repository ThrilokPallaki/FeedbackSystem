from django.forms import formset_facotry
from django import forms
from .models import *


class Question(forms.Form):
    Question = forms.CharField(disbaled=True)
    Ans = forms.CharField(max_length=200)


Question_formset = formset_factory(Question1, extra=Questions.objects.all().count())
