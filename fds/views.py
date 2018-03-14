# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Ranking, Questions, Answers
# Create your views here.
def fdsHome(request):
    return render(request, 'fds/index.html')


def ranking(request):
    if request.method=='POST':
        rank_name=request.POST['rank']
        rank = Ranking.objects.create(rank=rank_name)
	import pdb;pdb.set_trace()
        rank_id = rank.id
        return render(request, 'fds/thankingyou.html', {'rank_id':rank_id})
    return render(request, 'fds/index.html')


def questions(request, rank_id):
    rank = Ranking.objects.get(pk=rank_id)
    questions = Questions.objects.all()
    if request.method=='POST':
        for question in range(1, len(questions) + 1):
            q = Questions.objects.get(pk=question)
            answers = Answers.objects.create(rank=rank, questions=q, answers=request.POST['answer'+ str(question)])
        return HttpResponseRedirect(reverse('fds:goodbye'))
    return render(request, 'fds/questions.html', {'questions':questions, 'rank_id':rank_id})


def goodBye(request):
    return render(request,'fds/goodbye.html')


def ratingGraph(request):
    ecount, gcount, acount, wcount = 0,0,0,0
    rankings = Ranking.objects.all()
    for rank in rankings:
        if str(rank) == 'excellent':
            ecount +=1
        elif str(rank) == 'good':
            gcount +=1
        elif str(rank) == 'average':
            acount +=1
        elif str(rank) == 'worst':
            wcount +=1
    ranks = [ecount, gcount, acount, wcount]
    return render(request, 'fds/ratingchart.html', {'ranks':ranks})
