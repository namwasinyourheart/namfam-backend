# Generated by Django 5.0.7 on 2024-09-26 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aboutme", "0003_contact_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("institution", models.CharField(max_length=255)),
                ("degree", models.CharField(max_length=255)),
                ("duration", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
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
                    "education",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aboutme.education",
                    ),
                ),
                (
                    "professional_experience",
                    models.ManyToManyField(to="aboutme.professionalexperience"),
                ),
            ],
        ),
    ]
