# Generated by Django 3.0 on 2020-01-18 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LUT',
        ),
        migrations.AddField(
            model_name='worker',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]