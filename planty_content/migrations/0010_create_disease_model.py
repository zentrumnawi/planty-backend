# Generated by Django 3.0.11 on 2021-01-24 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0009_create_phenology_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
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
                    "oidium",
                    models.CharField(
                        choices=[("ja", "ja"), ("nein", "nein")],
                        max_length=4,
                        verbose_name="Anfälligkeite für Oidium",
                    ),
                ),
                (
                    "peronospora",
                    models.CharField(
                        choices=[("ja", "ja"), ("nein", "nein")],
                        max_length=4,
                        verbose_name="Anfälligkeit for Peronospora",
                    ),
                ),
                (
                    "botrytis",
                    models.CharField(
                        choices=[("ja", "ja"), ("nein", "nein")],
                        max_length=4,
                        verbose_name="Anfälligkeit für Botrytis",
                    ),
                ),
                (
                    "reblaus",
                    models.CharField(
                        choices=[
                            ("tolerant", "tolerant"),
                            ("resistent", "resistent"),
                            ("anfällig", "anfällig"),
                        ],
                        max_length=9,
                        verbose_name="Verhalten gegenüber Reblaus",
                    ),
                ),
                (
                    "wine",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="disease",
                        to="planty_content.Wine",
                        verbose_name="Rebe",
                    ),
                ),
            ],
            options={
                "verbose_name": "Krankheiten",
                "verbose_name_plural": "Krankheiten",
            },
        ),
    ]
