from django.contrib import admin
from django.urls import re_path
from gallery.views import index, projectPage, dashboard

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', index, name = 'index'),
    re_path(r'^projectpage/(?P<projectID>\w+)/$', projectPage, name = "projectpage"),
    re_path(r'^dashboard/', dashboard, name = "dashboard"),
]
