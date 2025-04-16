
from django.urls import path
from django.conf.urls.static import static
from settings.helper import BASE_DIR


from . import views

app_name="coolgv"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/<slug:slug>", views.LgvPage.as_view())
]  + static("media/", document_root="%s/media/" % BASE_DIR)