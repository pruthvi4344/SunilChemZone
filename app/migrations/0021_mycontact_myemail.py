# Generated by Django 5.1.4 on 2025-01-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='mycontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='myemail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
