from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("subjects", views.subjects, name="subjects"),
    path("reviews", views.reviews, name="reviews"),
    path("process", views.process, name="process"),
    path("services", views.services, name="services"),
    path("samples", views.samples, name="samples"),
]
