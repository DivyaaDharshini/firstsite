# Generated by Django 3.1.4 on 2020-12-04 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201204_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(null=True, upload_to='blog_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 4, 19, 32, 4, 727462)),
        ),
    ]
