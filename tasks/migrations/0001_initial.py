# Generated by Django 4.1.6 on 2023-05-14 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("boards", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, max_length=500)),
                ("attachment", models.FileField(blank=True, null=True, upload_to="")),
                ("duedate", models.DateField(blank=True, null=True)),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(0, "Low"), (1, "Medium"), (2, "High")], default=1
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "To Do"), (1, "In Progress"), (2, "Complete")],
                        default=0,
                    ),
                ),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="boards.board",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
