# Generated by Django 5.0.6 on 2024-07-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='job_type',
            field=models.CharField(default='Nothing Here', max_length=255),
        ),
    ]
