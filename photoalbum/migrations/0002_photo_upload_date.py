# Generated by Django 5.1.7 on 2025-03-11 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
