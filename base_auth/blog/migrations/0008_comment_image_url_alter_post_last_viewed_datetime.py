# Generated by Django 5.0.3 on 2024-05-12 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_last_viewed_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 20, 2, 16, 199913)),
        ),
    ]
