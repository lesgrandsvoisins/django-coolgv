from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import LgvPage


# Create your views here.
def index(request):
  context = {
    "title": "CooLgv",
    "lang_code": "fr",
    "description": "L'Autre est Une Chance."
  }
  return render(request, "coolgv/index.html",context)

class LgvPage(DetailView):
  model = LgvPage
  template_name = "coolgv/lgv_page.html"

