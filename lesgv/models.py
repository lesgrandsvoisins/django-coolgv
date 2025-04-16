from django.db import models
from markdownx.models import MarkdownxField
from django.urls import reverse
from solo.models import SingletonModel
# from markdownfield.models import MarkdownField, RenderedMarkdownField
# from markdownfield.validators import VALIDATOR_CLASSY


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    maintenance_mode = models.BooleanField(default=False)
    body = MarkdownxField()
    # body = MarkdownField(rendered_field='body_html', validator=VALIDATOR_CLASSY)
    # body_html = RenderedMarkdownField()
    description = models.TextField()

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"



class LgvPage(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownxField()
    # body = MarkdownField(rendered_field='body_html', validator=VALIDATOR_CLASSY)
    # body_html = RenderedMarkdownField()
    slug = models.SlugField(null=False, unique=True)  # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lgv_page", kwargs={"slug": self.slug})

