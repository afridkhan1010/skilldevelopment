# Generated by Django 3.2.12 on 2022-11-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_commentsmodel_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunchoflinks',
            name='followers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
