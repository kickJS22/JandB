from django.urls import path

from . import views

# Agrego un nombre para identificar las urls de esta app
app_name = "JandB"

urlpatterns = [
    path("JandB/", views.index, name="index"),
    path("about", views.home, name="home"),
    path("mywork", views.mywork, name="mywork"),
    path("knowledge", views.knowledge, name="knowledge")
]