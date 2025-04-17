
from django.urls import path
from django.conf.urls.static import static
from settings.helper import BASE_DIR


from . import views

app_name="gdv1"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/<slug:slug>", views.Gdv1Page.as_view())
]  + static("media/", document_root="%s/media/" % BASE_DIR)