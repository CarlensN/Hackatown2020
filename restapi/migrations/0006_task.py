# Generated by Django 3.0 on 2020-01-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20200118_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=45)),
                ('poster_id', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('HK', 'House Keeping'), ('REP', 'Repairs'), ('DEL', 'Del')], default='HK', max_length=3)),
                ('description', models.CharField(max_length=500)),
                ('dueDate', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longtitude', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
    ]
