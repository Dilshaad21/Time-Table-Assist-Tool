from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.file_upload),
    path('/time-table', views.time_table),
]