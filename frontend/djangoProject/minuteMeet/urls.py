from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recordingPage/", views.recordingPage, name="recordingPage"),
    path("archivePage/", views.archivePage, name="archivePage"),
    path("summaryPage/", views.summaryPage, name="summaryPage"),
    path("settingsPage/", views.settingsPage, name="settingsPage"),
    path('start_transcription/', views.start_transcription, name='start_transcription'),
    path('stop_transcription/', views.stop_transcription, name='stop_transcription'),
    path('upload_audio_transcription/', views.upload_audio_transcription, name='upload_audio_transcription'),
    path("stream_transcription/", views.stream_transcription, name="stream_transcription"),
    path("stop_transcription_stream/", views.stop_transcription_stream, name="stop_transcription_stream"),
    path("upload_transcript/", views.upload_transcript, name="upload_transcript"),
    path("download_summary/<str:file_name>/", views.download_summary, name="download_summary"),
    path("view_summary/<str:file_name>/", views.view_summary, name="view_summary"),
]
