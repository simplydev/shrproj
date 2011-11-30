from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from smrh.models import Contact,EmployeeDetails 
import settings
urlpatterns = patterns('',
    ('newcontact', 'smrh.views.contact'),
    ('reqcb', 'smrh.loginhandle.requestTokenCallBack'),
    ('hdllogin', 'smrh.loginhandle.checkUserLogin'),
    ('contacts',
        ListView.as_view(
            queryset=Contact.objects.order_by('-name')[:5],
            context_object_name='contact_list',
            template_name='smrh/tableAlone.html')),
      (r'^accounts/', include('gaeauth.urls')),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}
    ),
)
urlpatterns += patterns('',
    ('newemployee', 'smrh.views.employeeDetails'),
    ('empphdetai/(\d+)$', 'smrh.views.employeePhDetails'),
    ('empphdetai/(\d+)/$', 'smrh.views.employeePhDetails'),
    ('empadrdetai/(\d+)$', 'smrh.views.employeeAddrDetails'),
    ('empadrdetai/(\d+)/$', 'smrh.views.employeeAddrDetails'),
    ('employees',
        ListView.as_view(
            queryset=EmployeeDetails.objects.order_by('-lastName')[:5],
            context_object_name='employee_list',
            template_name='smrh/employeeTable.html')),
	('empphdetaivi/(\d+)/$','smrh.views.employeePhView'),
	('empaddrdetaivi/(\d+)/$','smrh.views.employeeAddrView')
	)






