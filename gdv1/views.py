from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Gdv1Page, SiteConfiguration
from html2text import html2text
from markdown import markdown
from .services import get_blog_posts, ProcessGhostParams

# Create your views here.
def index(request):
  config = SiteConfiguration.get_solo()
  context = {'page': 
    {
      "title_txt": html2text(config.title),
      "title_html": config.title,
      "lang_code": "fr",
      "description_txt": '. '.join(html2text(config.description).split('. ')[:3]), # + ('.' if '. ' in text else ''),
      "type_og": "website",
      "body_html": markdown(config.body),
    }
  }
  params = {"ghost_limit": 8}
  if config.ghost_post_tag:
    params["ghost_tag"] = config.ghost_post_tag
  context["posts"] = get_blog_posts(
    ProcessGhostParams(params)
  )
  context.update({
    "intro": markdown(config.intro),
    "section1": markdown(config.section1),
    "section2": markdown(config.section2),
    "section3": markdown(config.section3),
  })
  return render(request, "gdv1/index.html",context)

class Gdv1Page(DetailView):
  model = Gdv1Page
  template_name = "gdv1/gdv1_page.html"

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

