# Generated by Django 2.1.2 on 2018-11-14 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authBDF', '0018_auto_20181114_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateCreation',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 21, 41, 27, 785396)),
        ),
    ]
