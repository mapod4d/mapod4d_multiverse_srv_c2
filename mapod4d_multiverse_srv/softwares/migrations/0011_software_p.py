# Generated by Django 4.1.5 on 2023-04-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softwares', '0010_alter_software_so'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='p',
            field=models.CharField(default='s', max_length=2),
        ),
    ]
