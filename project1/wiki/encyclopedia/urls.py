from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pagename>", views.getpage, name="getpage"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("random/", views.randompage, name="randompage"),
    path("editpage/<str:pagetitle>", views.editpage, name="editpage")
]
