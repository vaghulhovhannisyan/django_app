# Generated by Django 5.0.2 on 2024-02-24 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_menu_name_alter_menu_named_url_alter_menu_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='title',
        ),
    ]
