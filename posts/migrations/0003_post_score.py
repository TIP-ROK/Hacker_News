# Generated by Django 3.2.9 on 2021-11-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211124_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
