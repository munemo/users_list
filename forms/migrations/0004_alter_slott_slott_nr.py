# Generated by Django 3.2.8 on 2021-10-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20211018_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slott',
            name='slott_nr',
            field=models.IntegerField(default=1),
        ),
    ]
