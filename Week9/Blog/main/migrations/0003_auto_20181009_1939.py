# Generated by Django 2.1.2 on 2018-10-09 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 19, 39, 45, 743285)),
        ),
    ]
