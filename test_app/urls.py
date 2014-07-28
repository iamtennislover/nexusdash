'''
Created on May 2, 2014

@author: admin
'''
from django.conf.urls import patterns, include, url

# My Imports
from .views import test_page

urlpatterns = patterns('',
    url(r'^$', test_page, name='test_page'),
)

