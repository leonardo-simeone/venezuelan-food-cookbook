from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


admin.site.register(Recipe)
admin.site.register(Comment)
