from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class Software(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    name = models.CharField(max_length=15, null=False, validators=[alphanumeric])
    link = models.URLField(default='')
    v1 = models.PositiveIntegerField(default=0, null=False)
    v2 = models.PositiveIntegerField(default=0, null=False)
    v3 = models.PositiveIntegerField(default=0, null=False)
    v4 = models.PositiveIntegerField(default=0, null=False)
    description = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.name
