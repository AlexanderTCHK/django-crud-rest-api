# Generated by Django 3.2 on 2021-05-03 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={},
        ),
        migrations.RemoveField(
            model_name='courses',
            name='created',
        ),
    ]