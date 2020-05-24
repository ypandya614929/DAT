# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from dat.models import Feedback

admin.site.site_header = 'Deep About Tweet'
admin.site.site_title = 'Deep About Tweet'
# Register your models here.
admin.site.register(Feedback)
#pip install imgkit
