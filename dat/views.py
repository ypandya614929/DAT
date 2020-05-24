#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from dat.forms import TextAnalyseForm, FeedbackForm, TweetAnalyseForm
from dat.models import Feedback, Tweetdata
#from .models.Tweetdata import *
from dat.result import Findemotion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    t_data = Tweetdata()
    if request.method == 'POST':
        MyTweetAnalyseForm = TweetAnalyseForm(request.POST)
        if MyTweetAnalyseForm.is_valid():
            text = MyTweetAnalyseForm.cleaned_data['data']
            if text[0] == '@':
                data, device, timedata = t_data.userdata(text[1:])
                if not data:
                    context = {'text': 'Username is Invalid'}
                    template = loader.get_template('home.html')
                    return HttpResponse(template.render(context, request))
                data_emotion = t_data.emotion(data)
                t_data.wordclouddata(data)
                t_data.devicechart(device)
                t_data.timechart(timedata)
                t_data.emotionpie(data_emotion)
                linkdata = t_data.findlink(data)

            else:
                data, device, timedata = t_data.hashdata(text)
                if not data:
                    context = {'text': 'Invalid Hashtag'}
                    template = loader.get_template('home.html')
                    return HttpResponse(template.render(context, request))
                data_emotion = t_data.emotion(data)
                t_data.wordclouddata(data)
                t_data.devicechart(device)
                t_data.timechart(timedata)
                t_data.emotionpie(data_emotion)
                linkdata = t_data.findlink(data)
            page = request.GET.get('page', 1)
            data_analyse = zip(data,data_emotion)
            context = {'text': text,'data' : data_analyse, 'linkdata': linkdata}
            template = loader.get_template('dash.html')
            return HttpResponse(template.render(context, request))
    else:
        return render(request, 'home.html')


def textanalyse(request):
    if request.method == 'POST':
        find_e = Findemotion()
        MyTextAnalyseForm = TextAnalyseForm(request.POST)
        if MyTextAnalyseForm.is_valid():
            text = MyTextAnalyseForm.cleaned_data['text']
            res = find_e.find_emotion(text)
            context = {'emotion': 'Emotion : ' + res.upper(),
                       'text': 'Text : ' + text}
            template = loader.get_template('textanalyse.html')
            return HttpResponse(template.render(context, request))
    else:
        return render(request, 'textanalyse.html')


def feedback(request):
    if request.method == 'POST':
        MyFeedbackForm = FeedbackForm(request.POST)
        if MyFeedbackForm.is_valid():
            feedback = Feedback()
            name = MyFeedbackForm.cleaned_data['name']
            email = MyFeedbackForm.cleaned_data['email']
            msg = MyFeedbackForm.cleaned_data['msg']
            v1 = Feedback.objects.filter(email=email).count()
            if v1 == 1:
                context = \
                    {'text': 'Already Feedback Given, Try With Different Email','check':False}
            else:
                feedback.name = name
                feedback.email = email
                feedback.msg = msg
                feedback.save()
                context = {'text': 'Thank You For Your Feedback','check':True}
            template = loader.get_template('feedback.html')
            return HttpResponse(template.render(context, request))
    else:
        return render(request, 'feedback.html')


def about(request):
    return render(request, 'about.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def dash(request):
    if not request.POST.get('data', False):
        return render(request, 'home.html')
