# Create your views here.
from django.views.generic import TemplateView


class My404View(TemplateView):
    # TODO: Find a better way and update 404.html html
    template_name = "404.html"
    
my404_page = My404View.as_view()

class HomeView(TemplateView):
    # TODO: Find a better way and update 404.html html
    template_name = "index.html"
    
home_page = HomeView.as_view()