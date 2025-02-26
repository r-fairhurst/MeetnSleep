from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recordingPage/", views.recordingPage, name="recordingPage"),
    path("archivePage/", views.archivePage, name="recordingPage"),
    path('start_transcription/', views.start_transcription, name='start_transcription'),
    path('stop_transcription/', views.stop_transcription, name='stop_transcription'),
    path('upload_audio_transcription/', views.upload_audio_transcription, name='upload_audio_transcription'),
    path("stream_transcription/", views.stream_transcription, name="stream_transcription")
]

