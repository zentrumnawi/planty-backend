# Generated by Django 3.0.11 on 2022-04-06 19:09

import django.db.models.deletion
from django.db import migrations, models

import planty_plant_content.models


class Migration(migrations.Migration):

    dependencies = [
        (
            "planty_plant_content",
            "0003_appearance_bark_blossom_fruit_habitus_leaf_root_sprout",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Function",
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
                    "sightings",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Sichtungsergebnisse",
                    ),
                ),
                (
                    "eco_net",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Eignung für die ökologische Vernetzung",
                    ),
                ),
                (
                    "roof_plant",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Eignung für Dach- und Kübelbepflanzung",
                    ),
                ),
                (
                    "breeding_prodcution",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Eignung für Zucht und Produktion",
                    ),
                ),
                (
                    "city_tree",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Eignung als Stadtbaum",
                    ),
                ),
                (
                    "city_application",
                    models.TextField(
                        blank=True,
                        help_text="Thema Klimabaum, Forst",
                        max_length=500,
                        null=True,
                        verbose_name="Eignung für die Verwendung in Städten",
                    ),
                ),
                (
                    "extra_notes",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Weitere Verwendungshinweise",
                    ),
                ),
                (
                    "extra_functions",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Weitere Funktionen",
                    ),
                ),
            ],
            options={"verbose_name": "Funktion", "verbose_name_plural": "Funktionen",},
        ),
        migrations.CreateModel(
            name="Habitat",
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
                    "area_of_life",
                    models.CharField(
                        blank=True,
                        help_text="Lebensbereich (ggf. Sekundärlebensbereiche) nach Kiermeier oder Hansen und Stahl (2006)",
                        max_length=100,
                        null=True,
                        verbose_name="Lebensbereiche",
                    ),
                ),
                (
                    "extra_areas",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Weitere Standorte",
                    ),
                ),
                (
                    "special_abilities",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Besondere Fähigkeiten am Standort",
                    ),
                ),
            ],
            options={"verbose_name": "Standorte", "verbose_name_plural": "Standorte",},
        ),
        migrations.CreateModel(
            name="HabitatFactors",
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
                    "micro_climate",
                    planty_plant_content.models.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("1", "bevorzugt Kühle"),
                                ("2", "hitzeempfindlich"),
                                ("3", "exponierte Lage"),
                                ("4", "geschützte Lage"),
                                ("5", "windgeschützte Lage"),
                                ("6", "windexponierte Lage"),
                                ("7", "Laubmull"),
                                ("8", "empfindlich auf Laubmull"),
                                ("9", "luftfeuchte Lage"),
                                ("10", "lufttrockene Lage"),
                                ("11", "wärmeliebend"),
                                ("12", "hitzeverträglich"),
                                ("13", "trockenwarm"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        help_text="Fähigkeiten, Ansprüche",
                        null=True,
                        size=None,
                        verbose_name="Mikroklima",
                    ),
                ),
                (
                    "room_climate",
                    models.TextField(
                        blank=True,
                        help_text="Für Innenräume",
                        max_length=500,
                        null=True,
                        verbose_name="Raumklimatische Faktoren ",
                    ),
                ),
                (
                    "frost_sensitivity",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Frostempfindlichkeit",
                    ),
                ),
                (
                    "hardy_zone",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1", "Z1 unter -45,5"),
                            ("2", "Z2 -45, 5 bis -40, 1"),
                            ("3", "Z3 -40, 1 bis -34, 5"),
                            ("4", "Z4 -34, 5 bis -28, 9"),
                            ("5", "Z5 -28, 8 bis -23, 4"),
                            ("6", "Z6 -23, 4 bis -17, 8"),
                            ("7", "Z7 -17, 8 bis -12, 3"),
                            ("8", "Z8 -12, 3 bis -6, 7"),
                            ("9", "Z9 -6, 7 bis -1, 2"),
                            ("10", "Z10 -1, 2 bis +4, 4"),
                            ("11", "Z11 über +4, 4"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Winterhärtezone",
                    ),
                ),
                (
                    "light",
                    planty_plant_content.models.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("1", "sonnig"),
                                ("2", "absonnig"),
                                ("3", "halbschattig"),
                                ("4", "schattig"),
                                ("5", "lichtschattig"),
                                ("6", "vollsonnig"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        null=True,
                        size=None,
                        verbose_name="Licht",
                    ),
                ),
                (
                    "extra_light",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Weitere Lichtfaktoren/ Besondere Fähigkeiten",
                    ),
                ),
                (
                    "soil_humidity",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Bodenfeuchte",
                    ),
                ),
                (
                    "extra_humidity",
                    models.TextField(
                        blank=True,
                        help_text="Beschreibung der Ansprüche an Feuchtigkeit",
                        max_length=500,
                        null=True,
                        verbose_name="Weitere Feuchtefaktoren/ Besondere Fähigkeiten",
                    ),
                ),
                (
                    "soil_reaction",
                    planty_plant_content.models.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("1", "sauer"),
                                ("2", "leicht sauer"),
                                ("3", "neutral"),
                                ("4", "leicht alkalisch"),
                                ("5", "alkalisch"),
                                ("6", "kalkreich"),
                                ("7", "basenreich"),
                                ("8", "kalkempfindlich"),
                                ("9", "kalkmeidend"),
                                ("10", "kalkfliehend"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        null=True,
                        size=None,
                        verbose_name="Bodenreaktion",
                    ),
                ),
                (
                    "nutrients",
                    planty_plant_content.models.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("1", "mager"),
                                ("2", "geringe Nährstoffansprüche"),
                                ("3", "mittlere Nährstoffansprüche"),
                                ("4", "hohe Nährstoffansprüche"),
                                ("5", "regelmäßige Nährstoffeinträge"),
                                ("6", "nitrophytisch"),
                            ],
                            max_length=2,
                        ),
                        blank=True,
                        null=True,
                        size=None,
                        verbose_name="Nährstoffe",
                    ),
                ),
                (
                    "extra_nutrients",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Weiteres zu Bodenreaktion und Nährstoffen/ Besondere Fähigkeiten ",
                    ),
                ),
                (
                    "soil",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Bodeneigenschaften",
                    ),
                ),
                (
                    "extra_soil",
                    models.TextField(
                        blank=True,
                        help_text="Bisher bekannte, geeignete Bodeneigenschaften aus Natur und Kultur",
                        max_length=500,
                        null=True,
                        verbose_name="Weitere Bodenfaktoren/ Besondere Fähigkeiten ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Standortfaktoren und Ansprüche",
                "verbose_name_plural": "Standortfaktoren und Ansprüche",
            },
        ),
        migrations.AlterModelOptions(
            name="bark",
            options={"verbose_name": "Rinde", "verbose_name_plural": "Rinden"},
        ),
        migrations.AlterModelOptions(
            name="blossom",
            options={"verbose_name": "Blüte", "verbose_name_plural": "Blüten"},
        ),
        migrations.AlterModelOptions(
            name="fruit",
            options={"verbose_name": "Frucht", "verbose_name_plural": "Früchte"},
        ),
        migrations.AlterModelOptions(
            name="habitus",
            options={"verbose_name": "Habitus", "verbose_name_plural": "Habita"},
        ),
        migrations.AlterModelOptions(
            name="leaf",
            options={"verbose_name": "Blatt", "verbose_name_plural": "Blätter"},
        ),
        migrations.AlterModelOptions(
            name="root",
            options={"verbose_name": "Wurzel", "verbose_name_plural": "Wurzeln"},
        ),
        migrations.AlterModelOptions(
            name="sprout",
            options={"verbose_name": "Trieb", "verbose_name_plural": "Triebe"},
        ),
        migrations.AlterField(
            model_name="blossom",
            name="extras",
            field=models.TextField(
                blank=True,
                help_text="",
                max_length=500,
                null=True,
                verbose_name="Weitere Merkmale ",
            ),
        ),
        migrations.AlterField(
            model_name="blossom",
            name="note_to_bloom",
            field=models.TextField(
                blank=True,
                help_text="",
                max_length=500,
                null=True,
                verbose_name="Hinweise zur Blütezeit",
            ),
        ),
        migrations.CreateModel(
            name="Application",
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
                    "appl_function",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="application",
                        to="planty_plant_content.Function",
                        verbose_name="Funktion",
                    ),
                ),
                (
                    "habitat",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="application",
                        to="planty_plant_content.Habitat",
                        verbose_name="Habitat",
                    ),
                ),
                (
                    "habitat_factors",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="application",
                        to="planty_plant_content.HabitatFactors",
                        verbose_name="Standortfaktoren und Ansprüche",
                    ),
                ),
                (
                    "plant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="application",
                        to="planty_plant_content.Plant",
                        verbose_name="Pflanze",
                    ),
                ),
            ],
            options={
                "verbose_name": "Verwendung",
                "verbose_name_plural": "Verwendungen",
            },
        ),
    ]
