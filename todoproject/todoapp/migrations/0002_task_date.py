# Generated by Django 4.2.3 on 2023-07-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-7-31'),
            preserve_default=False,
        ),
    ]