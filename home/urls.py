from django.urls import path
from . import views

from home.models import Subject, Set


urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("reviews", views.reviews, name="reviews"),
    path("process", views.process, name="process"),
    path("services", views.services, name="services"),
    path("samples", views.samples, name="samples"),
    path("mcqs", views.mcqs, name="mcqs"),
    path("mcqs/<int:entry>", views.sets, name="sets"),
    path("mcqs/<int:entry>/<int:set>", views.questions, name="questions"),

    path("search", views.search, name="search"),

    path("sitemap.xml", views.sitemap, name="sitemap"),
]
