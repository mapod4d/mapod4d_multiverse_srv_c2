# Generated by Django 4.1.5 on 2023-01-20 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_users'),
        ('multiverse', '0004_metaverse_description_metaverse_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metaverse',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='metaverse', to='projects.project'),
            preserve_default=False,
        ),
    ]
