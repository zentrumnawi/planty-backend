# Generated by Django 3.0.11 on 2022-12-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0011_auto_20221122_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='climate_suitability',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Einschätzung Klimawandeltauglichkeit'),
        ),
    ]
