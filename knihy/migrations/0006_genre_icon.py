# Generated by Django 4.2.1 on 2024-02-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihy', '0005_genre_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]