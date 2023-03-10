# Generated by Django 4.1.5 on 2023-03-02 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapod4d', '0001_initial'),
        ('multiverse', '0011_metaverseversion_unique_range_mapod4d_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='metaverseversion',
            name='unique_range_mapod4d',
        ),
        migrations.RemoveConstraint(
            model_name='metaverseversion',
            name='unique_fromv_mapod4d',
        ),
        migrations.RemoveConstraint(
            model_name='metaverseversion',
            name='unique_to',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='frommv1',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='frommv2',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='frommv3',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='frommv4',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='tomv1',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='tomv2',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='tomv3',
        ),
        migrations.RemoveField(
            model_name='metaverseversion',
            name='tomv4',
        ),
        migrations.AddField(
            model_name='metaverseversion',
            name='fmver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='metaverseversions_from', to='mapod4d.mapod4dversion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metaverseversion',
            name='tmver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='metaverseversions_to', to='mapod4d.mapod4dversion'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='metaverseversion',
            constraint=models.UniqueConstraint(models.F('metaverse'), models.F('fmver'), models.F('tmver'), name='metaverse_version_range'),
        ),
        migrations.AddConstraint(
            model_name='metaverseversion',
            constraint=models.UniqueConstraint(models.F('metaverse'), models.F('fmver'), name='metaverse_version_fromver'),
        ),
        migrations.AddConstraint(
            model_name='metaverseversion',
            constraint=models.UniqueConstraint(models.F('metaverse'), models.F('tmver'), name='metaverse_version_tover'),
        ),
    ]
