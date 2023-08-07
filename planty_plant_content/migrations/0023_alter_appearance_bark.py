# Generated by Django 3.2.16 on 2023-07-13 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0022_auto_20230713_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearance',
            name='bark',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appearance', to='planty_plant_content.bark', verbose_name='Rinde'),
        ),
    ]
