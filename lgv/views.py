from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import LgvPage, SiteConfiguration
from html2text import html2text
from markdown import markdown
from .services import get_blog_posts, ProcessGhostParams

def ifValF(val,func):
  if not val:
    return False
  return func(val)

# Create your views here.
def index(request):
  config = SiteConfiguration.get_solo()
  context = {'page': 
    {
      "title_txt": html2text(config.title),
      "title_html": config.title,
      "lang_code": "fr",
      "description_txt": ifValF(config.description,lambda x: '. '.join(html2text(x).split('. ')[:3])), # + ('.' if '. ' in text else '')
      "type_og": "website",
      "body_html": ifValF(config.body, lambda x: markdown(x)),
      "favicon": config.favicon,
      "favicon_svg": config.favicon_svg,
    }
  }
  params = {"ghost_limit": 8}
  if config.ghost_post_tag:
    params["ghost_tag"] = config.ghost_post_tag
  context["posts"] = get_blog_posts(
    ProcessGhostParams(params)
  )
  context.update({
    "intro": ifValF(config.intro, lambda x: markdown(x)),
    "section1": ifValF(config.section1, lambda x: markdown(x)),
    "section2": ifValF(config.section2, lambda x: markdown(x)),
    "section3": ifValF(config.section3, lambda x: markdown(x)),
  })
  return render(request, "lgv/index.html",context)

class LgvPage(DetailView):
  model = LgvPage
  template_name = "lgv/lgv_page.html"

  def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    context["title_txt"] = html2text(markdown(context["object"].title))
    context["title_html"] = ifValF(context["object"].title, lambda x: markdown(x))
    context["lang_code"] = "fr"
    context["description_txt"] = ifValF(context["object"].body, lambda x: '. '.join(html2text(markdown(x)).split('. ')[:3])), # + ('.' if '. ' in text else '')
    context["type_og"] = "website",
    context["body_html"] = ifValF(context["object"].body, lambda x: markdown(x))
    return context

