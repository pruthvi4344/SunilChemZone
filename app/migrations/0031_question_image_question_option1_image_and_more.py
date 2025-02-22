# Generated by Django 5.1.4 on 2025-02-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_quiz_time_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option1_image',
            field=models.ImageField(blank=True, null=True, upload_to='option_images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option2_image',
            field=models.ImageField(blank=True, null=True, upload_to='option_images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option3_image',
            field=models.ImageField(blank=True, null=True, upload_to='option_images/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option4_image',
            field=models.ImageField(blank=True, null=True, upload_to='option_images/'),
        ),
    ]
