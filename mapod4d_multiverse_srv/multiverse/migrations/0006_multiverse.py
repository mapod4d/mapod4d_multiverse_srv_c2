# Generated by Django 4.1.5 on 2023-01-20 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiverse', '0005_metaverse_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiverse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapod4d_id', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('server', models.URLField(default='http://infosrv0000.mapod4d.it')),
                ('port', models.IntegerField(default='80', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('description', models.TextField(default='', max_length=200)),
            ],
        ),
    ]
