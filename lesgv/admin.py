from django.contrib import admin

# Register your models here.
from .models import LgvPage

class LgvPageAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)

admin.site.register(LgvPage, LgvPageAdmin)
