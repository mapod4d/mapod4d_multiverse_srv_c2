# Generated by Django 4.1.5 on 2023-01-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_users'),
        ('multiverse', '0006_multiverse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaverse',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metaverses', to='projects.project'),
        ),
    ]
