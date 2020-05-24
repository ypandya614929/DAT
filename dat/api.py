from tastypie.resources import ModelResource
from tastypie.constants import ALL
from . import swagger_details
from tastypie.utils import trailing_slash
from django.conf.urls import url
from django.http import HttpResponse
from tastypie.utils.mime import determine_format, build_content_type
from .result import Findemotion
from .tweetdata import Tweetdata
import json
from datetime import datetime
#from urllib.parse import urlparse
from tastypie.serializers import Serializer
from .models import Feedback
find_e = Findemotion()
t_data = Tweetdata()


class FeedbackResource(ModelResource):
    class Meta:
        serializer = Serializer()
        queryset = Feedback.objects.all()


class EmotionResource(ModelResource):
    class Meta:
        serializer = Serializer()
        extra_actions = [
           swagger_details.EmotionActivity,
        ]

    def prepend_urls(self):
        params = (self._meta.resource_name, trailing_slash())
        return [
            url(r"^(?P<resource_name>%s)/emotion%s$" % params, self.wrap_view('emotion_activity'),
                name="api_emotion_activity"),
        ]

    def emotion_activity(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        tstart = datetime.now()
        
        temp = request.body.decode("utf-8")
        result = find_e.find_emotion(temp)
        
        tstop = datetime.now()
        print ("Total Time For Text Analysis : ",tstop-tstart)

        return HttpResponse(
            content="Text : "+temp+"\nResult : "+result,
            status=200
        )

class UserEmotionResource(ModelResource):
    class Meta:
        serializer = Serializer()
        extra_actions = [
           swagger_details.UserEmotionActivity,
        ]

    def prepend_urls(self):
        params = (self._meta.resource_name, trailing_slash())
        return [
            url(r"^(?P<resource_name>%s)/useremotion%s$" % params, self.wrap_view('useremotion_activity'),
                name="api_useremotion_activity"),
        ]

    def useremotion_activity(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        tstart = datetime.now()

        temp = request.body.decode("utf-8")
        l=t_data.userdata(temp)
        res=dict()

        tstop1 = datetime.now()

        print ("Data Fetching time : ",tstop1-tstart)

        for i in l:
            res[i]=find_e.find_emotion(i)

        tstop = datetime.now()

        print ("Result Generation time : ",tstop-tstop1)
        print ("Total Time For User Analysis : ",tstop-tstart)

        return HttpResponse(
            content=json.dumps(res),
            content_type='application/json',
            status=200
        )

class HashEmotionResource(ModelResource):
    class Meta:
        serializer = Serializer()
        allowed_methods = ['post']
        extra_actions = [
           swagger_details.HashEmotionActivity,
        ]

    def prepend_urls(self):
        params = (self._meta.resource_name, trailing_slash())
        return [
            url(r"^(?P<resource_name>%s)/hashemotion%s$" % params, self.wrap_view('hashemotion_activity'),
                name="api_hashemotion_activity"),
        ]

    def hashemotion_activity(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        tstart = datetime.now()

        temp = request.body.decode("utf-8")
        l=t_data.hashdata(temp)
        res=dict()

        tstop1 = datetime.now()

        print ("Data Fetching time : ",tstop1-tstart)

        for i in l:
            res[i]=find_e.find_emotion(i)

        tstop = datetime.now()

        print ("Result Generation time : ",tstop-tstop1)
        print ("Total Time For Hashtag Analysis: ",tstop-tstart)

        return HttpResponse(
            content=json.dumps(res),
            content_type='application/json',
            status=200
        )

class TimechartResource(ModelResource):
    class Meta:
        serializer = Serializer()
        allowed_methods = ['post']
        extra_actions = [
           swagger_details.TimechartActivity,
        ]

    def prepend_urls(self):
        params = (self._meta.resource_name, trailing_slash())
        return [
            url(r"^(?P<resource_name>%s)/timechart%s$" % params, self.wrap_view('timechart_activity'),
                name="api_timechart_activity"),
        ]

    def timechart_activity(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        tstart = datetime.now()

        temp = request.body.decode("utf-8")
        res=t_data.timedata(temp)
        
        tstop = datetime.now()

        print ("Data Fetching time & Result Generation : ",tstop-tstart)

        return HttpResponse(
            content=res,
            status=200
        )

class UrlResource(ModelResource):
    serializer = Serializer()
    class Meta:
        allowed_methods = ['post']
        extra_actions = [
           swagger_details.UrlActivity,
        ]

    def prepend_urls(self):
        params = (self._meta.resource_name, trailing_slash())
        return [
            url(r"^(?P<resource_name>%s)/url%s$" % params, self.wrap_view('url_activity'),
                name="api_url_activity"),
        ]

    def url_activity(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        tstart = datetime.now()

        temp = request.body.decode("utf-8")
        res=t_data.urldata(temp)
        
        tstop = datetime.now()

        print ("Data Fetching time & Result Generation : ",tstop-tstart)

        return HttpResponse(
            content=json.dumps(res),
            content_type='application/json',
            status=200
        )

class SourceResource(ModelResource):
    class Meta:
        serializer = Serializer()
        allowed_methods = ['post']
        extra_actions = [
           swagger_details.SourceActivity,
        ]

    def prepend_urls(self):
        params = (self._meta.resource_name, trailing_slash())
        return [
            url(r"^(?P<resource_name>%s)/source%s$" % params, self.wrap_view('source_activity'),
                name="api_source_activity"),
        ]

    def source_activity(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        tstart = datetime.now()

        temp = request.body.decode("utf-8")
        res=t_data.sourcedata(temp)
        
        tstop = datetime.now()

        print ("Data Fetching time & Result Generation : ",tstop-tstart)

        return HttpResponse(
            content=json.dumps(res),
            content_type='application/json',
            status=200
        )