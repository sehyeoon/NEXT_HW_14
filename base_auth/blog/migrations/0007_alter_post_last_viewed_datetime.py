# Generated by Django 5.0.3 on 2024-05-12 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 19, 37, 17, 877054)),
        ),
    ]
