# Generated by Django 4.1.6 on 2023-09-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[(0, "Low"), (1, "Medium"), (2, "High")], default=0
            ),
        ),
    ]
