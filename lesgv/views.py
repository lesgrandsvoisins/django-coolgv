from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    "title": "LesGV",
    "lang_code": "fr",
    "description": "L'Autre est Une Chance."
  }
  return render(request, "lesgv/index.html",context)