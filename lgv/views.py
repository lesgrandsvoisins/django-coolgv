from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import LgvPage, SiteConfiguration
from html2text import html2text
from markdown import markdown

# Create your views here.
def index(request):
  config = SiteConfiguration.get_solo()
  context = {'page': 
    {
      "title_txt": html2text(config.site_name),
      "title_html": config.site_name,
      "lang_code": "fr",
      "description_txt": '. '.join(html2text(config.description).split('. ')[:3]), # + ('.' if '. ' in text else ''),
      "type_og": "website",
      "body_html": markdown(config.body),
    }
  }
  return render(request, "lgv/index.html",context)

class LgvPage(DetailView):
  model = LgvPage
  template_name = "lgv/lgv_page.html"

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    context["title_txt"] = html2text(markdown(context["object"].title))
    context["title_html"] = markdown(context["object"].title)
    context["lang_code"] = "fr"
    context["description_txt"] = '. '.join(html2text(markdown(context["object"].body)).split('. ')[:3]), # + ('.' if '. ' in text else '')
    context["type_og"] = "website",
    context["body_html"] = markdown(context["object"].body)
    return context
  

