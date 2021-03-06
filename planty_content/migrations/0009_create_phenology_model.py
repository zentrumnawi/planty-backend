# Generated by Django 3.0.11 on 2021-01-24 15:05

import django.db.models.deletion
import solid_backend.content.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0008_create_properties_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Phenology",
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
                    "budding",
                    solid_backend.content.fields.FromToConcatField(
                        blank=True,
                        default="",
                        from_choices=(
                            ("sehr früh", "sehr früh"),
                            ("früh", "früh"),
                            ("mittel", "mittel"),
                            ("spät", "spät"),
                            ("sehr spät", "sehr spät"),
                        ),
                        max_length=100,
                        to_choices=(
                            ("sehr früh", "sehr früh"),
                            ("früh", "früh"),
                            ("mittel", "mittel"),
                            ("spät", "spät"),
                            ("sehr spät", "sehr spät"),
                        ),
                        verbose_name="Austrieb",
                    ),
                ),
                (
                    "bloom",
                    solid_backend.content.fields.FromToConcatField(
                        blank=True,
                        default="",
                        from_choices=(
                            ("sehr früh", "sehr früh"),
                            ("früh", "früh"),
                            ("mittel", "mittel"),
                            ("spät", "spät"),
                            ("sehr spät", "sehr spät"),
                        ),
                        max_length=100,
                        to_choices=(
                            ("sehr früh", "sehr früh"),
                            ("früh", "früh"),
                            ("mittel", "mittel"),
                            ("spät", "spät"),
                            ("sehr spät", "sehr spät"),
                        ),
                        verbose_name="Blütezeitpunkt",
                    ),
                ),
                (
                    "ripening",
                    solid_backend.content.fields.FromToConcatField(
                        blank=True,
                        default="",
                        from_choices=(
                            ("sehr früh", "sehr früh"),
                            ("früh", "früh"),
                            ("mittel", "mittel"),
                            ("spät", "spät"),
                            ("sehr spät", "sehr spät"),
                        ),
                        max_length=100,
                        to_choices=(
                            ("sehr früh", "sehr früh"),
                            ("früh", "früh"),
                            ("mittel", "mittel"),
                            ("spät", "spät"),
                            ("sehr spät", "sehr spät"),
                        ),
                        verbose_name="Reifezeit",
                    ),
                ),
                (
                    "wine",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="phenology",
                        to="planty_content.Wine",
                        verbose_name="Rebe",
                    ),
                ),
            ],
            options={
                "verbose_name": "Phänologie",
                "verbose_name_plural": "Phänologien",
            },
        ),
    ]
