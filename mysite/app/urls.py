from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.ResourceCreateView.as_view(), name="index"),
]