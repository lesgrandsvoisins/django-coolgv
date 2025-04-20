from django.contrib import admin

# Register your models here.
from .models import DjangoLgvPage, DjangoLgvSiteConfiguration
from markdownx.admin import MarkdownxModelAdmin
from solo.admin import SingletonModelAdmin

class SingleModelAdmin(MarkdownxModelAdmin,SingletonModelAdmin):
  pass

# class DjangoLgvPageAdmin(admin.ModelAdmin):
#     list_display = ("title", "body",)

admin.site.register(DjangoLgvPage, MarkdownxModelAdmin)
admin.site.register(DjangoLgvSiteConfiguration, SingleModelAdmin)
