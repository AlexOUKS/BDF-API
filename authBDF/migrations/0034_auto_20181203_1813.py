# Generated by Django 2.1.2 on 2018-12-03 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authBDF', '0033_auto_20181203_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateCreation',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 3, 18, 13, 40, 514473)),
        ),
    ]
