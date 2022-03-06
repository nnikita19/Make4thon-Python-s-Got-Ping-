from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('takeInput/',views.takeInput,name="takeInput"),
    path('answer/',views.answer,name="answer"),
]