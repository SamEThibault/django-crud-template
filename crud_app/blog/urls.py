from django.urls import path
from . import views

# paths within the blog application
urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
