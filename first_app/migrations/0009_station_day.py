# Generated by Django 2.0.7 on 2019-02-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_auto_20190210_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='day',
            field=models.IntegerField(default=0),
        ),
    ]
