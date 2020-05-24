from django.conf.urls import *
from dat import views
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin
from tastypie.api import Api
from dat.api import *

e_api = Api(api_name='Emotion')
e_api.register(EmotionResource())
e_api.register(UserEmotionResource())
e_api.register(HashEmotionResource())
e_api.register(TimechartResource())
e_api.register(UrlResource())
e_api.register(SourceResource())
e_api.register(FeedbackResource())


urlpatterns = [

    #define the url getdata that we have written inside form
    url(r'^$', views.index, name='index'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^about/', views.about, name='about'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^textanalyse/', views.textanalyse, name='textanalyse'),
    url(r'^dashboard/', views.dash, name='dashboard'),
    #url(r'^textanalysis/', views.textanalysis, name='textanalysis'),
]
