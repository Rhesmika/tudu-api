# Generated by Django 4.1.6 on 2023-02-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.IntegerField(choices=[(0, 'Requested'), (1, 'Accepted'), (2, 'Declined')], default=0),
        ),
    ]
