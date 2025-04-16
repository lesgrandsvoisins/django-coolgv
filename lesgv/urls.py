
from django.urls import path

from . import views

app_name="lesgv"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/<slug:slug>", views.LgvPage.as_view())
]