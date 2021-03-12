# Generated by Django 3.0.11 on 2021-01-24 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0004_create_grown_leaf_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grape",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "density",
                    models.CharField(
                        choices=[
                            ("lockerbeerig", "lockerbeerig"),
                            ("kompakt", "kompakt"),
                        ],
                        max_length=12,
                        verbose_name="Dichte",
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("sehr klein", "sehr klein"),
                            ("klein", "klein"),
                            ("mittel", "mittel"),
                            ("groß", "groß"),
                            ("sehr groß", "sehr groß"),
                        ],
                        max_length=10,
                        verbose_name="Größe ohne Stiel",
                    ),
                ),
                (
                    "form",
                    models.CharField(
                        choices=[
                            ("zylindrisch", "zylindrisch"),
                            ("zylindrisch geschultert", "zylindrisch geschultert"),
                            ("konisch", "konisch"),
                            ("konisch geschultert", "konisch geschultert"),
                        ],
                        max_length=24,
                        verbose_name="Form",
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="Besonderheiten",
                    ),
                ),
                (
                    "wine",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="grape",
                        to="planty_content.Wine",
                        verbose_name="Rebe",
                    ),
                ),
            ],
            options={"verbose_name": "Traube", "verbose_name_plural": "Trauben",},
        ),
    ]