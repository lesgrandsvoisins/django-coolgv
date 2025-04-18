from django.db import models
from markdownx.models import MarkdownxField
from django.urls import reverse
from solo.models import SingletonModel
from .fields import TitleMarkdownxFormField
from .utils import strip_markdown
from django.core.validators import FileExtensionValidator


class TitleMarkdownxField(MarkdownxField):
    def formfield(self, **kwargs):
        defaults = {'form_class': TitleMarkdownxFormField}
        defaults.update(kwargs)
        return super(TitleMarkdownxField, self).formfield(**defaults)

class SiteConfiguration(SingletonModel):
    title = TitleMarkdownxField(max_length=255, default='Titre du site')
    maintenance_mode = models.BooleanField(default=False)
    body = MarkdownxField(null=True,blank=True)
    section1 = MarkdownxField(null=True,blank=True)
    section2 = MarkdownxField(null=True,blank=True)
    section3 = MarkdownxField(null=True,blank=True)
    intro    = MarkdownxField(null=True,blank=True)
    ghost_post_tag = models.SlugField(null=True, unique=False, blank=True) 
    footer1 = MarkdownxField(null=True,blank=True)
    footer2 = MarkdownxField(null=True,blank=True)
    description = MarkdownxField(null=True,blank=True)
    favicon = models.ImageField(upload_to="favicon/",null=True,blank=True)
    # favicon_svg = models.FileField(upload_to="favicon/",null=True, validators=[FileExtensionValidator(allowed_extensions=['svg'])],blank=True)
    favicon_svg = models.FileField(upload_to="favicon/",validators=[FileExtensionValidator(allowed_extensions=['svg'])],null=True,blank=True)

    def __str__(self):
        return "Configuration du site"

    class Meta:
        verbose_name = "Configuration du site"

class Gdv1Page(models.Model):
    title = TitleMarkdownxField()
    body = MarkdownxField()
    slug = models.SlugField(null=False, unique=True) 

    def __str__(self):
        return "page/%s : %s" % (self.slug, strip_markdown(self.title))

    def get_absolute_url(self):
        return reverse("gdv1_page", kwargs={"slug": self.slug})

# class Gdv1HomePage(Gdv1Page):
