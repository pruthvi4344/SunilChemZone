# Generated by Django 5.1.4 on 2025-01-06 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_std_chapter_standard_rename_std_standard_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='standard',
            new_name='std',
        ),
        migrations.RenameField(
            model_name='standard',
            old_name='name',
            new_name='std',
        ),
        migrations.RenameField(
            model_name='studymaterial',
            old_name='chapter',
            new_name='chapters',
        ),
    ]
