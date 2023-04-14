from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


class CookbookAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'instructions':
            kwargs['widget'] = TinyMCE()
        return super(CookbookAdmin, self).formfield_for_dbfield(db_field,**kwargs)


admin.site.register(Recipe, CookbookAdmin)
admin.site.register(Comment)
