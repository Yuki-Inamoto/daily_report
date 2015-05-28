from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_queryset, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^write/$', views.write_report, name='write'),
    url(r'^user/$', views.user_pages, name='user_pages'),
    url(r'^re-write/(?P<report_id>\d+)/$', views.re_write, name='re-write'),
    url(r'^delete/(?P<report_id>\d+)/$', views.delete, name='delete'),
    url(r'^search/$', views.search, name='search'),
    url(r'^read-report/(?P<report_id>\d+)/$', views.read_report, name='read_reoprt'),

]