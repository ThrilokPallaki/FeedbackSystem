# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Questions, Answers, Users
# Create your views here.
# def fdsHome(request):
#     return render(request, 'fds/index.html')

def fdsuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        usermobile = request.POST['usermobile']
        userrank = request.POST['userranking']
        user = Users.objects.create(user_name=username, user_email=useremail, mobile_no=usermobile, rank=userrank)
        user_id = user.id
        return render(request, 'fds/thankingyou.html', {'user':user_id})
    return render(request, 'fds/fds.html')


# def ranking(request):
#     if request.method=='POST':
#         rank_name=request.POST['rank']
#         rank = Ranking.objects.create(rank=rank_name)
#         rank_id = rank.id
#         return render(request, 'fds/thankingyou.html', {'rank_id':rank_id})
#     return render(request, 'fds/index.html')
#
#
def questions(request, user_id):
    user = Users.objects.get(pk=user_id) # Getting user object
    questions = Questions.objects.all() # Getting question object
    if request.method == 'POST':
        for question in range(1, len(questions) + 1):
            q = Questions.objects.get(pk=question)
            answers = Answers.objects.create(user=user, question=q, answer=request.POST['answer'+ str(question)], rank=request.POST['userrank'+str(question)])
        return HttpResponseRedirect(reverse('fds:goodbye'))
    return render(request, 'fds/questions.html', {'questions':questions, 'user':user_id, 'ranks':['Excellent', 'Good', 'Average', 'Worst']})


def goodBye(request):
    return render(request,'fds/goodbye.html')



# def ratingGraph(request):
#     ecount, gcount, acount, wcount = 0,0,0,0
#     rankings = Ranking.objects.all()
#     for rank in rankings:
#         if str(rank) == 'excellent':
#             ecount +=1
#         elif str(rank) == 'good':
#             gcount +=1
#         elif str(rank) == 'average':
#             acount +=1
#         elif str(rank) == 'worst':
#             wcount +=1
#     ranks = [ecount, gcount, acount, wcount]
#     return render(request, 'fds/ratingchart.html', {'ranks':ranks})
