# Generated by Django 2.1.2 on 2018-11-14 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authBDF', '0013_auto_20181112_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateCreation',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 13, 6, 57, 281526)),
        ),
    ]
