from django.urls import path
from .views import extract_names_view

urlpatterns = [
    path("extract-names/", extract_names_view, name="extract_names"),
]
