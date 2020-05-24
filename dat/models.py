#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import shutil
from django.db import models
import tweepy
import sys
import random
import datetime
import operator
from collections import Counter
from .result import Findemotion
import wordcloud
import csv
from wordcloud import WordCloud
from IPython.display import Image,display
from collections import OrderedDict
from operator import itemgetter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import re
from rake_nltk import Rake
import googlemaps
from django.conf import settings as djangoSettings

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
gmaps = googlemaps.Client(key='')

class Feedback(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    msg = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.name,self.msg)

class Tweetdata(object):

    def hashdata(self, tag):
        device = list()
        data1 = list()
        timedata = list()
        try:
            udata = tweepy.Cursor(api.search,lang='en', q=tag).items(100)
        except:
            return
        for tweet in udata:
            device.append(tweet.source)
            data1.append(tweet.text)
            timedata.append(str(tweet.created_at))

        return data1, device, timedata



    def userdata(self, uid):
        data1 = list()
        device = list()
        timedata = list()
        try:
        	udata = api.user_timeline(screen_name = uid, count = 90)
        except:
        	return [],[],[]
        for tweet in udata:
            data1.append(tweet.text)
            device.append(tweet.source)
            timedata.append(str(tweet.created_at))
        return data1, device, timedata



    def emotion(self, data):
        data1 = list()
        find_e = Findemotion()
        for data in data:
            data1.append(find_e.find_emotion(data))

        return data1



    def wordclouddata(self, data):
        w = WordCloud(width = 700, height = 400,background_color="white",
    		max_words=2000).generate(" ".join(data))
        w.to_image().save('wordcloud_demo.jpg')
        shutil.move("wordcloud_demo.jpg", "dat/static/dash/assets/images/wordcloud_demo.jpg")




    def devicechart(self, device):
        counts = Counter(device)
        lable = list()
        val = list()
        for (key, value) in counts.items():
            lable.append(key)
            val.append(value)
        fig_size = plt.rcParams['figure.figsize']
        fig_size[0] = 10
        fig_size[1] = 9
        plt.rcParams['font.size'] = 12
        plt.rcParams['figure.figsize'] = fig_size
        if len(lable) > 5:
            lable = lable[0:5]
            val = val[0:5]
        else:
            pass
        plt.pie(
            val,
            labels=lable,
            shadow=True,
            startangle=90,
            autopct='%1.1f%%',
            wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
            )
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('sourcedevice_demo')
        plt.close()
        shutil.move("sourcedevice_demo.png", "dat/static/dash/assets/images/sourcedevice_demo.png")



    def timechart(self, timedata):

        d = dict()
        t = list()

        for i in range(1, 25):
            if i < 10:
                i = '0' + str(i)
            if str(i) not in d:
                d[str(i)] = 0

        for i in timedata:
            s = str(i).split(' ')
            s1 = str(s[1]).strip('\']').split(':')
            d1 = s1[0]
            if int(d1) < 10:
                d1 = '0' + str(d1)
            if d1 not in d:
                d[d1] = 0
            else:
                d[d1] = d[d1] + 1
        sorted_d = sorted(d.items(), key=operator.itemgetter(0))
        for (key, value) in sorted_d:
            t.append(value)
        #print sum(t)
        label = [
            '1 - 3',
            '4 - 6',
            '7 - 9',
            '10 - 12',
            '13 - 15',
            '16 - 18',
            '19 - 21',
            '22 - 24',
            ]
        val = [
            sum(t[0:3]),
            sum(t[3:6]),
            sum(t[6:9]),
            sum(t[9:12]),
            sum(t[12:15]),
            sum(t[15:18]),
            sum(t[18:21]),
            sum(t[21:24]),
            ]
        y_pos = np.arange(len(label))
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = 8
        fig_size[1] = 5
        plt.rcParams["figure.figsize"] = fig_size
        plt.bar(y_pos, val, align='center',width=0.8)
        plt.xticks(y_pos, label)
        plt.ylabel('No of Tweets')
        plt.title('Time of Tweets')
        plt.savefig('timechart_demo')
        plt.close()
        shutil.move('timechart_demo.png','dat/static/dash/assets/images/timechart_demo.png')


    def emotionpie(self, data):
        counts = Counter(data)
        labels = list()
        sizes = list()
        for (key, value) in counts.items():
            sizes.append(value)
            labels.append(str(key))
        fig_size = plt.rcParams['figure.figsize']
        fig_size[0] = 10
        fig_size[1] = 9
        plt.rcParams['font.size'] = 15
        plt.rcParams['figure.figsize'] = fig_size
        plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            shadow=True,
            startangle=90,
            wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
            )
        plt.savefig('emotion_demo')
        plt.close()
        shutil.move('emotion_demo.png','dat/static/dash/assets/images/emotion_demo.png')


    def findlink(self, data):
        linkdata=list()
        for temp in data:
            temp_list = temp.split(" ")
            for i in temp_list:
                i = i.encode('ascii', 'replace')
                if i.startswith(b'http://') or i.startswith(b'https://') :
                	linkdata.append(i.decode())
        return linkdata
