# Generated by Django 3.2.12 on 2022-11-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='followers',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
