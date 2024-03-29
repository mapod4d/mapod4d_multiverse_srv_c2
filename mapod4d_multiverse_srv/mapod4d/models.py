from django.db import models

from django.contrib import admin
from django.core.validators import RegexValidator, MaxValueValidator
from .managers import Mapod4dVersionManager


class Mapod4d(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    name = models.CharField(max_length=21, null=False, unique=True, validators=[alphanumeric])
    description = models.TextField(max_length=200, default='')
 
    def __str__(self):
        return self.name


class Mapod4dVersion(models.Model):
    link = models.URLField(default='')
    v1 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v2 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v3 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v4 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    p = models.CharField(max_length=2, default="s", null=False)
    bricks = models.PositiveIntegerField(default=1, null=False)
    compressed = models.BooleanField(default=True, null=False)
    mapod4d = models.ForeignKey('Mapod4d', on_delete=models.CASCADE)

    objects = Mapod4dVersionManager()

    def get_sversion(self):
        return '{v1:03d}{v2:03d}{v3:03d}{v4:03d}'.format(
                v1=self.v1, v2=self.v2, v3=self.v3, v4=self.v4)

    class Meta:
        constraints = [
            models.UniqueConstraint('mapod4d', 'v1', 'v2', 'v3', 'v4',  name='mapod4d_version'),
        ]
 
    def __str__(self):
        name = "_".join([
                self.mapod4d.name,
                str(self.v1),
                str(self.v2),
                str(self.v3),
                str(self.v4)
        ])
        return name 

