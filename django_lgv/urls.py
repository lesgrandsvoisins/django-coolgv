
from django.urls import path
from django.conf.urls.static import static
from settings.helper import BASE_DIR


from . import views

app_name="django_lgv"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/<slug:slug>", views.DjangoLgvPage.as_view())
]  + static("media/", document_root="%s/media/" % BASE_DIR)