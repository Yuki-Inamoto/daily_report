from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_queryset, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^write/$', views.write_report, name='write'),
    url(r'^user/$', views.user_pages, name='user_pages'),
]