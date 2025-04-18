from django.shortcuts import render
from .models import CropSeason

def crop_season_view(request):
    # Get all CropSeason data, ordered by year
    seasons = CropSeason.objects.all().order_by('year')
    return render(request, 'records/crop_season.html', {'seasons': seasons})
