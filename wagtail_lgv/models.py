from django.db import models
from wagtail.fields import RichTextField
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from wagtail.models import Page
from wagtail.search import index
from wagtail.admin.panels import FieldPanel

from grapple.models import GraphQLString

rich_text_settings = ['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'blockquote']

@register_setting
class WagtailLgvSettings(BaseSiteSetting):
    Footer1 = RichTextField(features=rich_text_settings,blank=True,null=True)
    Footer2 = RichTextField(features=rich_text_settings,blank=True,null=True)
    # wagtail_title = TitleMarkdownxField(max_length=255, default='Titre du site')
    maintenance_mode = models.BooleanField(default=False,blank=True,null=True)
    # body = RichTextField(features=rich_text_settings,blank=True,null=True)
    # section1 = RichTextField(features=rich_text_settings,blank=True,null=True)
    # section2 = RichTextField(features=rich_text_settings,blank=True,null=True)
    # section3 = RichTextField(features=rich_text_settings,blank=True,null=True)
    # intro    = RichTextField(features=rich_text_settings,blank=True,null=True)
    # ghost_post_tag = models.SlugField(null=True, unique=False, blank=True) 
    # footer1 = RichTextField(features=rich_text_settings,blank=True,null=True)
    # footer2 = RichTextField(features=rich_text_settings,blank=True,null=True)
    # description = RichTextField(features=rich_text_settings,blank=True,null=True)
    favicon = models.ImageField(upload_to="favicon/",null=True,blank=True)
    # # favicon_svg = models.FileField(upload_to="favicon/",null=True, validators=[FileExtensionValidator(allowed_extensions=['svg'])],blank=True)
    # favicon_svg = models.FileField(upload_to="favicon/",validators=[FileExtensionValidator(allowed_extensions=['svg'])],null=True,blank=True)

class WagtailLgvHomePage(Page):
  intro    = RichTextField(features=rich_text_settings,blank=True,null=True)
  body = RichTextField(features=rich_text_settings,blank=True,null=True)
  section1 = RichTextField(features=rich_text_settings,blank=True,null=True)
  section2 = RichTextField(features=rich_text_settings,blank=True,null=True)
  section3 = RichTextField(features=rich_text_settings,blank=True,null=True)
  ghost_post_tag = models.SlugField(null=True, unique=False, blank=True) 
  description = RichTextField(features=rich_text_settings,blank=True,null=True)
  header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


  search_fields = Page.search_fields + [
      index.SearchField('intro'),
      index.SearchField('body'),
      index.SearchField('section1'),
      index.SearchField('section2'),
      index.SearchField('section3'),
  ]

  content_panels = Page.content_panels + [
      FieldPanel('intro'),
      FieldPanel('body'),
      FieldPanel('section1'),
      FieldPanel('section2'),
      FieldPanel('section3'),
      FieldPanel('description'),
      FieldPanel('header_image'),
      FieldPanel('ghost_post_tag'),
  ]

  graphql_fields = [
      GraphQLString('intro'),
      GraphQLString('body'),
      GraphQLString('section1'),
      GraphQLString('section2'),
      GraphQLString('section3'),
      GraphQLString('description'),
      GraphQLString('header_image'),
      GraphQLString('ghost_post_tag'),
  ]
