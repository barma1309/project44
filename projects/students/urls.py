from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'students.views.home', name='home'),
    url(r'^group/$', 'students.views.group', name='group'),
    url(r'^table/$', 'students.views.table', name='table'),
    url(r'^groups/$', 'students.views.groups_list', name='groups'),


# Students urls
    url(r'^$', 'students.views.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students_add',name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_delete', name='students_delete'),
    url(r'^students/test/$', 'students.views.students_list', name='studentstest'),
# Groups urls
    url(r'^groups/$', 'students.views.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups_delete', name='groups_delete'),
    url(r'^admin/', include(admin.site.urls))

]