from django.contrib import admin

# Register your models here.
from .models import LgvPage, SiteConfiguration
from markdownx.admin import MarkdownxModelAdmin
from solo.admin import SingletonModelAdmin



# class LgvPageAdmin(admin.ModelAdmin):
#     list_display = ("title", "body",)

admin.site.register(LgvPage, MarkdownxModelAdmin)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
