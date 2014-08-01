# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
import json


class My404View(TemplateView):
    # TODO: Find a better way and update 404.html html
    template_name = "404.html"
    
my404_page = My404View.as_view()

class RunQueryView(TemplateView):
    '''Returns JSON data based on querying the sql db, after getting the latest data
    This JSON gets used by dashboard.*.js files
    '''

    def get(self, request, *args, **kwargs):
        '''
        Overriding get to return only JSON.
        '''
        context = {} # self.get_context_data(**kwargs)
        
        if self.request.GET.get('module') == 'hostnames':
            # Return the table body
            # http://www.djangobook.com/en/2.0/chapter04.html
            from hostnames.views import HostNamesView
            from django.template import loader, Context
            t = loader.get_template('hostnames/hostnames.table.html')
            c = Context(HostNamesView().get_context_data())
            tbody_html = t.render(c)
            context['data'] = tbody_html

        return HttpResponse(json.dumps(context), content_type="application/json")
    
run_query = RunQueryView.as_view()