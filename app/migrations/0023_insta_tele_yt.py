# Generated by Django 5.1.4 on 2025-01-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_mycontact_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='insta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=50)),
                ('iname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tele', models.CharField(max_length=50)),
                ('tname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='yt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt', models.CharField(max_length=50)),
                ('yname', models.CharField(max_length=50)),
            ],
        ),
    ]
