# Generated by Django 4.1.5 on 2023-04-21 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapod4d', '0005_mapod4dversion_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapod4dversion',
            name='test',
        ),
    ]