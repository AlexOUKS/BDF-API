# Generated by Django 2.1.2 on 2018-12-05 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authBDF', '0034_auto_20181203_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateCreation',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 5, 10, 33, 4, 471399)),
        ),
    ]
