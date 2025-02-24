from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recordingPage/", views.recordingPage, name="recordingPage"),
    path("archivePage/", views.archivePage, name="recordingPage")
]