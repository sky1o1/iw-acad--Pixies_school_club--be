# Generated by Django 3.0.8 on 2020-08-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_club_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
