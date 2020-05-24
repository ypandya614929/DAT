try:
    from django.conf.urls import include, url
except ImportError:
	pass

from tastypie_swagger.views import SwaggerView, ResourcesView, SchemaView


urlpatterns = [
    url(r'^$', SwaggerView.as_view(), name='index'),
    url(r'^resources/$', ResourcesView.as_view(), name='resources'),
    url(r'^schema/(?P<resource>\S+)$', SchemaView.as_view()),
    url(r'^schema/$', SchemaView.as_view(), name='schema'),
]
