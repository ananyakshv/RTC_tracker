from django.urls import path
from .views import crop_season_view

urlpatterns = [
    path('seasons/', crop_season_view, name='crop_season'),
]
