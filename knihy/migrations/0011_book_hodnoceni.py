# Generated by Django 5.0.1 on 2024-02-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihy', '0010_remove_book_genre_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='hodnoceni',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]
