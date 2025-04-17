from django.db import models
from markdownx.models import MarkdownxField
from django.urls import reverse
from solo.models import SingletonModel
from .fields import TitleMarkdownxFormField
from .utils import strip_markdown

class TitleMarkdownxField(MarkdownxField):
    def formfield(self, **kwargs):
        defaults = {'form_class': TitleMarkdownxFormField}
        defaults.update(kwargs)
        return super(TitleMarkdownxField, self).formfield(**defaults)

class SiteConfiguration(SingletonModel):
    title = TitleMarkdownxField(max_length=255, default='Titre du site')
    maintenance_mode = models.BooleanField(default=False)
    body = MarkdownxField()
    description = MarkdownxField()

    def __str__(self):
        return "Configuration du site"

    class Meta:
        verbose_name = "Configuration du site"

class LgvPage(models.Model):
    title = TitleMarkdownxField()
    body = MarkdownxField()
    slug = models.SlugField(null=False, unique=True) 

    def __str__(self):
        return "page/%s : %s" % (self.slug, strip_markdown(self.title))

    def get_absolute_url(self):
        return reverse("lgv_page", kwargs={"slug": self.slug})

