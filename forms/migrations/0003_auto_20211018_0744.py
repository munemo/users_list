# Generated by Django 3.2.8 on 2021-10-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slott',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slott_nr', models.CharField(max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='apartment_nr',
            field=models.IntegerField(default=1),
        ),
    ]
