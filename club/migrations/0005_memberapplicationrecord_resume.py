# Generated by Django 3.0.7 on 2020-08-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20200829_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberapplicationrecord',
            name='resume',
            field=models.ImageField(blank=True, null=True, upload_to='images/resume'),
        ),
    ]