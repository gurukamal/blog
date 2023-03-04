# Generated by Django 4.1.7 on 2023-03-03 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Incident",
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
                (
                    "incident_id",
                    models.CharField(blank=True, max_length=100, unique=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(blank=True, default="", max_length=100)),
                ("body", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPEN", "Open"),
                            ("INPROGRESS", "Inprogress"),
                            ("CLOSED", "Closed"),
                        ],
                        default="OPEN",
                        max_length=20,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("HIGH", "High"),
                            ("MEDIUM", "Medium"),
                            ("LOW", "Low"),
                        ],
                        default="LOW",
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incidents",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["created"]},
        )
    ]
