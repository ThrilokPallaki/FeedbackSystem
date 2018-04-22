# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from .models import Questions, Answers, Users


class UserCreateView(CreateView):
    model = Users
    fields = ['user_name', 'user_email', 'mobile_no', 'rank']


class ThankingYouView(TemplateView):
    template_name = 'fds/thankingyou.html'

def questions(request, user):
    user = Users.objects.get(pk=user) # Getting user object
    questions = Questions.objects.all() # Getting question object

    if request.method == 'POST':
        for question in range(1, len(questions) + 1):
            q = Questions.objects.get(pk=question)
            answers = Answers.objects.create(user=user, question=q, answer=request.POST['answer'+ str(question)], rank=request.POST['userrank'+str(question)])

        return HttpResponseRedirect(reverse('fds:goodbye'))

    return render(request, 'fds/questions.html', {'questions':questions, 'user':user.id, 'ranks':['Excellent', 'Good', 'Average', 'Worst']})


class GoodByeView(TemplateView):
    template_name = 'fds/goodbye.html'


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


class DashboardView(TemplateView):
    template_name = 'fds/dashboard.html'

    def get_context_data(self, **kwargs):
        main_ecount = main_gcount = main_acount = main_wcount = 0
        q1_ecount = q1_gcount = q1_acount = q1_wcount = 0
        q2_ecount = q2_gcount = q2_acount = q2_wcount = 0
        q3_ecount = q3_gcount = q3_acount = q3_wcount = 0
        context = super(DashboardView, self).get_context_data(**kwargs)
        main_ranks = Users.objects.values_list('rank', flat=True)

        for rank in main_ranks:
            if str(rank) == 'Excellent':
                main_ecount += 1
            elif str(rank) == 'Good':
                main_gcount += 1
            elif str(rank) == 'Average':
                main_acount += 1
            elif str(rank) == 'Worst':
                main_wcount += 1

        q1 = Questions.objects.get(pk=1)
        q1_ranks = q1.answers_set.all()

        for rank in q1_ranks:
            if str(rank.rank) == 'Excellent':
                q1_ecount += 1
            elif str(rank.rank) == 'Good':
                q1_gcount += 1
            elif str(rank.rank) == 'Average':
                q1_acount += 1
            elif str(rank.rank) == 'Worst':
                q1_wcount += 1

        q2 = Questions.objects.get(pk=2)
        q2_ranks = q2.answers_set.all()

        for rank in q2_ranks:
            if str(rank.rank) == 'Excellent':
                q2_ecount += 1
            elif str(rank.rank) == 'Good':
                q2_gcount += 1
            elif str(rank.rank) == 'Average':
                q2_acount += 1
            elif str(rank.rank) == 'Worst':
                q2_wcount += 1

        q3 = Questions.objects.get(pk=3)
        q3_ranks = q3.answers_set.all()

        for rank in q3_ranks:
            if str(rank.rank) == 'Excellent':
                q3_ecount += 1
            elif str(rank.rank) == 'Good':
                q3_gcount += 1
            elif str(rank.rank) == 'Average':
                q3_acount += 1
            elif str(rank.rank) == 'Worst':
                q3_wcount += 1

        context['main_ranks'] = [main_ecount, main_gcount, main_acount, main_wcount]
        context['question1_ranks'] = [q1_ecount, q1_gcount, q1_acount, q1_wcount]
        context['question2_ranks'] = [q2_ecount, q2_gcount, q2_acount, q2_wcount]
        context['question3_ranks'] = [q3_ecount, q3_gcount, q3_acount, q3_wcount]
        return context
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


#def goodBye(request):
#    return render(request,'fds/goodbye.html')


# def ranking(request):
#     if request.method=='POST':
#         rank_name=request.POST['rank']
#         rank = Ranking.objects.create(rank=rank_name)
#         rank_id = rank.id
#         return render(request, 'fds/thankingyou.html', {'rank_id':rank_id})
#     return render(request, 'fds/index.html')
#
#


# class QuestionsView(CreateView):
#     model = Answers
#     fields = ['user', 'question', 'answer', 'rank']


# class AnswersFormView(FormView):
#     template_name = 'questionform.html'
#     form_class = UsersAnswers
#     success_url = '/goodbye/'
#
#     def get_form_kwargs(self):
#         kwargs = super(AnswersFormView, self).get_form_kwargs()
#         kwargs['user'] = self.kwargs['user']
#         return kwargs
#
#     def post(request, *args, **kwargs):
#         form = users()
#         form_valid(form)
