# Generated by Django 5.0.1 on 2024-02-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihy', '0012_alter_book_hodnoceni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='hodnoceni',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
