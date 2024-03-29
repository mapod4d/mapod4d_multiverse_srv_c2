# Generated by Django 4.1.5 on 2023-04-22 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiverse', '0016_remove_metaverseversion_metaverse_version_range_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metaverseversion',
            name='compress',
        ),
        migrations.AddField(
            model_name='metaverseversion',
            name='compressed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='metaverseversion',
            name='metaverse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metaverseversions', to='multiverse.metaverse'),
        ),
    ]
