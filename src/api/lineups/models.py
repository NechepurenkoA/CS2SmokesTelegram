from django.core.validators import FileExtensionValidator
from django.db import models

from lineups import constants


class Lineup(models.Model):

    class Maps(models.TextChoices):
        MIRAGE = "mirage"

    class GrenadeTypes(models.TextChoices):
        EXPLOSIVE = "explosive"
        SMOKE = "smoke"
        FLASH = "flash"

    title = models.CharField(max_length=constants.MAX_FIELD_LENGTH)
    map = models.CharField(choices=Maps.choices, default=Maps.MIRAGE)
    grenade_type = models.CharField(
        choices=GrenadeTypes.choices, default=GrenadeTypes.SMOKE
    )
    author = models.CharField(
        max_length=constants.MAX_FIELD_LENGTH, default=constants.DEFAULT_AUTHOR_VALUE
    )
    video = models.FileField(
        upload_to=constants.URL_TO_UPLOAD_VIDEOS,
        validators=[
            FileExtensionValidator(
                [
                    constants.EXTENSION_TO_VALIDATE,
                ]
            ),
        ],
    )
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
