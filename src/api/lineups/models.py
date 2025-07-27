from django.db import models


class Lineup(models.Model):

    class Maps(models.TextChoices):
        MIRAGE = "Mirage"

    class GrenadeTypes(models.TextChoices):
        EXPLOSIVE = "Explosive"
        SMOKE = "Smoke"
        FLASH = "Flash"

    title = models.CharField(max_length=255)
    map = models.CharField(max_length=255, choices=Maps.choices)
    grenade_type = models.CharField(choices=GrenadeTypes.choices)
    author = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title