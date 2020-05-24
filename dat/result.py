# coding: utf-8

from . import tokenizer
from .trainer import Trainer
from .classifier import Classifier
import csv

newsTrainer = Trainer(tokenizer)

with open('wordmatch.csv', 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]

for item in data:
    newsTrainer.train(item[0], item[1])

newsClassifier = Classifier(newsTrainer.data, tokenizer)

class Findemotion(object):

    def find_emotion(self, temp):
        s=temp.lower() #for text from user
        if not s:
            return "null, please enter some text"

        l2=s.split(" ") #convert text strings into words
        l3=list()  #list that have classification label
        d1=dict()  #label with its value

        for word in l2:
            classification = newsClassifier.classify(word.lower())
            l3.append(classification)

        total=list()

        for i in range(0,len(l2)):
            for j in range(0,11):
                key=l3[i][j][0]
                value=l3[i][j][1]
        	    #print key,value
                if key not in d1:
                    d1[key]=value
                else:
                    d1[key]=d1[key]+value

        l=list() #list containing final result with label and value
        for key,value in d1.items():
            l.append((key,format(value,'f')))

        res=list() #sorting according to value
        #   print ("\n",d1,"\n")
        for i in l:
            res.append(i[1])

        #print "\nOutput : ",l[res.index(max(res))][0],"\n"
        return l[res.index(max(res))][0]
