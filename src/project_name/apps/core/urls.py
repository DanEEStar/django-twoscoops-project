from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^glyphicons/$', TemplateView.as_view(template_name='glyphicons.html')),
)

