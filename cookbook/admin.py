from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


class CookbookAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Recipe, CookbookAdmin)
admin.site.register(Comment)
