# Generated by Django 5.1.4 on 2025-01-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_chapters_chapter_rename_standard_chapter_std_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='std',
            new_name='standard',
        ),
        migrations.RenameField(
            model_name='standard',
            old_name='std',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='studymaterial',
            old_name='chapters',
            new_name='chapter',
        ),
    ]
