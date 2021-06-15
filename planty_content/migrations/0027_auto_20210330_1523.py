# Generated by Django 3.0.11 on 2021-03-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planty_content", "0026_auto_20210330_1518"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sprout",
            name="hairy",
            field=models.CharField(
                blank=True,
                choices=[("ja", "ja"), ("nein", "nein")],
                max_length=4,
                null=True,
                verbose_name="Behaarung des Triebs",
            ),
        ),
        migrations.AlterField(
            model_name="sprout",
            name="tip_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("offen", "offen"),
                    ("halb offen bis offen", "halb offen bis offen"),
                    ("halb offen", "halb offen"),
                    ("geschlossen bis halboffen", "geschlossen bis halboffen"),
                    ("geschlossen", "geschlossen"),
                ],
                max_length=25,
                null=True,
                verbose_name="Typ der Triebspitze",
            ),
        ),
    ]
