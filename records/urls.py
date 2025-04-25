from django.urls import path
from .views import crop_season_view
from .views import ownership_view
from . import views

urlpatterns = [
    path('ownership/', ownership_view, name='ownership'),
    path('seasons/', views.crop_season_view, name='crop_season_view'),
]

