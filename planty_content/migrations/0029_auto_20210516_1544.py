# Generated by Django 3.0.11 on 2021-05-16 13:44

import solid_backend.content.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0028_delete_ant_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grape",
            name="density",
            field=solid_backend.content.fields.FromToConcatField(
                blank=True,
                default="",
                from_choices=(
                    (None, "---------"),
                    ("lockerbeerig", "lockerbeerig"),
                    ("mitteldicht", "mitteldicht"),
                    ("kompakt", "kompakt"),
                ),
                max_length=30,
                to_choices=(
                    (None, "---------"),
                    ("lockerbeerig", "lockerbeerig"),
                    ("mitteldicht", "mitteldicht"),
                    ("kompakt", "kompakt"),
                ),
                verbose_name="Dichte",
            ),
        ),
        migrations.AlterField(
            model_name="grape",
            name="form",
            field=solid_backend.content.fields.FromToConcatField(
                blank=True,
                default="",
                from_choices=(
                    (None, "---------"),
                    ("zylindrisch", "zylindrisch"),
                    ("konisch", "konisch"),
                    ("kegelförmig", "kegelförmig"),
                    ("walzenförmig", "walzenförmig"),
                ),
                max_length=55,
                to_choices=(
                    (None, "---------"),
                    ("zylindrisch", "zylindrisch"),
                    ("konisch", "konisch"),
                    ("kegelförmig", "kegelförmig"),
                    ("walzenförmig", "walzenförmig"),
                ),
                verbose_name="Form",
            ),
        ),
        migrations.AlterField(
            model_name="grape",
            name="shouldered",
            field=models.CharField(
                blank=True,
                choices=[("ja", "ja"), ("nein", "nein"), ("teilweise", "teilweise")],
                max_length=9,
                null=True,
                verbose_name="Geschultert",
            ),
        ),
        migrations.AlterField(
            model_name="grape",
            name="size",
            field=models.CharField(
                blank=True,
                choices=[
                    ("sehr klein", "sehr klein"),
                    ("klein", "klein"),
                    ("mittel", "mittel"),
                    ("groß", "groß"),
                    ("sehr groß", "sehr groß"),
                ],
                max_length=10,
                null=True,
                verbose_name="Größe ohne Stiel",
            ),
        ),
    ]
