# Generated by Django 5.0.2 on 2024-02-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_remove_menu_name_remove_menu_named_url_menu_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
