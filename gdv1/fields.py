from markdownx.fields import MarkdownxFormField

from .widgets import TitleMarkdownxWidget

class TitleMarkdownxFormField(MarkdownxFormField):
  def __init__(self, *args, **kwargs):
    super(MarkdownxFormField, self).__init__(*args, **kwargs)
    self.widget = TitleMarkdownxWidget()
