# Generated by Django 4.2.1 on 2024-02-19 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knihy', '0006_genre_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['genre']},
        ),
    ]
