# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Questions, Answers, Users
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.
# def fdsHome(request):
#     return render(request, 'fds/index.html')


# def fdsuser(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         useremail = request.POST['useremail']
#         usermobile = request.POST['usermobile']
#         userrank = request.POST['userranking']
#         user = Users.objects.create(user_name=username, user_email=useremail, mobile_no=usermobile, rank=userrank)
#         user_id = user.id
#         return HttpResponseRedirect(reverse('fds:thankyou', kwargs={'user': user_id}))
#     return render(request, 'fds/fds.html')


class UserCreateView(CreateView):
    model = Users
    fields = ['user_name', 'user_email', 'mobile_no', 'rank']


class ThankingYouView(TemplateView):
    template_name = 'fds/thankingyou.html'


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


class GoodByeView(TemplateView):
    template_name = 'fds/goodbye.html'


#def goodBye(request):
#    return render(request,'fds/goodbye.html')


class RatingGraphView(TemplateView):
    template_name = 'fds/ratingchart.html'

    def get_context_data(self, **kwargs):
        ecount, gcount, acount, wcount = [0,0,0,0]
        context = super(RatingGraphView, self).get_context_data(**kwargs)
        ranks = Users.objects.values_list('rank', flat=True)
        for rank in ranks:
            if str(rank) == 'Excellent':
                ecount += 1
            elif str(rank) == 'Good':
                gcount += 1
            elif str(rank) == 'Average':
                acount += 1
            elif str(rank) == 'Worst':
                wcount += 1
        context['ranks'] = [ecount, gcount, acount, wcount]
        return context
