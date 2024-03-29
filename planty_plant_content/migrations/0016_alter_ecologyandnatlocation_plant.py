# Generated by Django 3.2.16 on 2023-05-20 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0015_plant_tree_node'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecologyandnatlocation',
            name='plant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ecology_and_natlocation', to='planty_plant_content.plant', verbose_name='Pflanze'),
        ),
    ]
