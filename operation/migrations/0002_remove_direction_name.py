# Generated by Django 4.0.1 on 2022-02-01 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='name',
        ),
    ]
