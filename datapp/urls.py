"""datapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import dat
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
#import .settings
from django.conf.urls import url, include
from django.contrib import admin
from dat.urls import e_api
from django.conf.urls.static import static
from django.conf import settings
#from dat import apiurl

static_view = never_cache(serve)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dat.urls')),
    url(r'^api/',include(e_api.urls,namespace="yash")),
]
