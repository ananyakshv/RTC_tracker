from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    area = models.FloatField()
    transaction_type = models.CharField(max_length=100)
    transaction_year = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class CropSeason(models.Model):
    SEASON_CHOICES = (
        ('ಮುಂಗಾರ', 'Mungaru'),
        ('ಹಿಂಗಾರು', 'Hingaru'),
    )
    year = models.CharField(max_length=10)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES)
    farmers = models.ManyToManyField(Owner)

    def __str__(self):
        return f"{self.year} - {self.season}"
