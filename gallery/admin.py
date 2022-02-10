from django.contrib import admin
from . import models

admin.site.register(models.Projects)
admin.site.register(models.MediaTypes)
admin.site.register(models.Media)