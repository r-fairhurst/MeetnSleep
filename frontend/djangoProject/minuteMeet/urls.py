from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recordingPage/", views.recordingPage, name="recordingPage"),
    path("archivePage/", views.archivePage, name="recordingPage"),
    path('start_transcription/', views.start_transcription, name='start_transcription'),
    path('upload_audio_transcription/', views.upload_audio_transcription, name='upload_audio_transcription'),
]

