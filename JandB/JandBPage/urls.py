from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mywork", views.mywork, name="mywork"),
    path("knowledge", views.knowledge, name="knowledge")
]