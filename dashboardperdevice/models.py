from django.db import models
import datetime

# TODO
# ShowProcessCpu
# ShowInterface

class ShowSysResource(models.Model):
    '''Many-to-one relationship. e.i Many ShowSysResources for one HostName
    # https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_one/
    '''
    hostname = models.ForeignKey('hostnames.HostNames')
    polling_timestamp = models.FloatField()
    raw_json_dump = models.CharField(max_length=1000*1000)       # Use jsn = json.dumps(mydict), strng = json.loads(jsn)
    cpu_user = models.FloatField()
    cpu_kernel = models.FloatField()
    memory_used = models.CharField(max_length=20)
    memory_total = models.CharField(max_length=20)
    memory_free = models.CharField(max_length=20)
    
    def __unicode__(self):
        return str(datetime.datetime.fromtimestamp(self.polling_timestamp))