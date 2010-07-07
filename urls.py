from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^app1/', include('app1.urls')),
    (r'^app2/', include('app2.urls')),
)
