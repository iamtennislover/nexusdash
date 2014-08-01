from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class DashboardPerDeviceView(TemplateView):
    # TODO
    template_name = "dashboardperdevice/dashboardperdevice.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        hostname = kwargs.get('hostname')
        print 'testhostname', hostname
        return self.render_to_response(context)
    
dashboard_view = DashboardPerDeviceView.as_view()
