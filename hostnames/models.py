from django.db import models
from django.contrib.auth.models import User

class HostNames(User):
    '''
    This is a model for View seen by index.html Network Dashboard Table
    This model is updated by the LoginForm
    NOTE: Do not make primary_key a non-integer item: https://code.djangoproject.com/ticket/14881
    '''
    url = models.URLField(unique=True)
    is_online = models.BooleanField(default=False)
    is_healthy = models.BooleanField(default=False)
    hostname = models.CharField(unique=True, max_length=100)        # This is simply hostname extraction from url using urlparse
    
    def __unicode__(self):
        return self.hostname