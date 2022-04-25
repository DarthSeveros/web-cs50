from django.urls import URLPattern


from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="index"),
    path("brian", views.brian, name="brian")
]