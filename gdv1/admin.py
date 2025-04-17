from django.contrib import admin

# Register your models here.
from .models import Gdv1Page, SiteConfiguration
from markdownx.admin import MarkdownxModelAdmin
from solo.admin import SingletonModelAdmin

class SingleModelAdmin(MarkdownxModelAdmin,SingletonModelAdmin):
  pass

# class Gdv1PageAdmin(admin.ModelAdmin):
#     list_display = ("title", "body",)

admin.site.register(Gdv1Page, MarkdownxModelAdmin)
admin.site.register(SiteConfiguration, SingleModelAdmin)
