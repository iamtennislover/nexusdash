from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# My imports
from django.conf import settings
from .views import home_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nexusdash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home_page, name='home_page'),
    
    # Apps
    url(r'^admin/', include(admin.site.urls)),
    url('^test/', include('test_app.urls')),
)

# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
