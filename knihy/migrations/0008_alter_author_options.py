# Generated by Django 4.2.1 on 2024-02-19 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knihy', '0007_alter_genre_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
    ]
